"""Defines protocols and ABC for Assigned exercises page."""

from abc import ABC, abstractmethod

from typing_extensions import override

from wse.apps.main.pages.assignations import (
    AssignationsModelFeatureProto,
    AssignationsModelObserveProto,
    AssignationsViewFeatureProto,
    AssignationsViewObserveProto,
)
from wse.feature.base.mixins import (
    AddObserverMixin,
    ModelObserverMixin,
    ModelT,
)
from wse.feature.base.mvc import (
    BasePageController,
    Model,
    View,
    ViewT,
)
from wse.feature.shared.schemas.exercise import ExerciseInfo, ExerciseMeta

# Model


class AssignationsModelFeature(
    ABC,
    AssignationsModelFeatureProto,
):
    """Abstract base class for assigned page model feature."""

    @abstractmethod
    @override
    def fetch_exercises(self) -> None:
        """Fetch assigned exercises."""

    @abstractmethod
    @override
    def fetch_exercise(
        self,
        assignation_id: str,
    ) -> ExerciseMeta | None:
        """Fetch assigned exercise meta."""


class BaseAssignationsModel(
    Model,
    AddObserverMixin,
    AssignationsModelFeature,
    ABC,
):
    """Abstract base class for Assigned exercises model."""


class AssignationsModelObserver(
    ABC,
    AssignationsModelObserveProto,
):
    """Abstract base class for assigned model event observer."""

    @abstractmethod
    @override
    def exercises_updated(self, exercises: list[ExerciseInfo]) -> None:
        """Update view on update exercises event."""


# View


class AssignationsViewFeature(
    ABC,
    AssignationsViewFeatureProto,
):
    """Abstract base class for assigned view feature."""

    @abstractmethod
    @override
    def update_exercises(self, exercises: list[ExerciseInfo]) -> None:
        """Update exercises to display."""

    @abstractmethod
    @override
    def exercise_selected(self, value: str) -> None:
        """Notify that exercise selected."""


class BaseAssignationsView(
    AssignationsViewFeature,
    View,
    ModelObserverMixin[ModelT],
    ABC,
):
    """Abstract base class for Assigned exercise page."""


class AssignationsViewObserver(
    ABC,
    AssignationsViewObserveProto,
):
    """Abstract base class for assigned view event observer."""

    @abstractmethod
    @override
    def exercise_selected(self, value: str) -> None:
        """Handle exercise selected event."""


# Controller


class BaseAssignationsController(
    AssignationsModelObserver,
    AssignationsViewObserver,
    BasePageController[ViewT],
    ABC,
):
    """Abstract base class for Assigned exercises page."""
