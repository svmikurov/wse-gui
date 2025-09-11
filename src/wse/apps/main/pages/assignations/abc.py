"""Defines protocols and ABC for Assigned exercises page."""

from abc import ABC, abstractmethod

from wse.feature.base.mixins import (
    AddObserverMixin,
    ModelObserverMixin,
    ModelT,
)
from wse.feature.base.mvc import (
    Model,
    PageControllerABC,
    View,
    ViewT,
)
from wse.feature.shared.schemas.exercise import ExerciseInfo, ExerciseMeta

# Model


class AssignationsModelFeature(
    ABC,
):
    """Abstract base class for assigned page model feature."""

    @abstractmethod
    def fetch_exercises(self) -> None:
        """Fetch assigned exercises."""

    @abstractmethod
    def fetch_exercise(
        self,
        assignation_id: str,
    ) -> ExerciseMeta | None:
        """Fetch assigned exercise meta."""


class AssignationsModelABC(
    Model,
    AddObserverMixin,
    AssignationsModelFeature,
    ABC,
):
    """Abstract base class for Assigned exercises model."""


class AssignationsModelObserver(
    ABC,
):
    """Abstract base class for assigned model event observer."""

    @abstractmethod
    def exercises_updated(self, exercises: list[ExerciseInfo]) -> None:
        """Update view on update exercises event."""


# View


class AssignationsViewFeatureABC(
    ABC,
):
    """Abstract base class for assigned view feature."""

    @abstractmethod
    def update_exercises(self, exercises: list[ExerciseInfo]) -> None:
        """Update exercises to display."""

    @abstractmethod
    def exercise_selected(self, value: str) -> None:
        """Notify that exercise selected."""


class AssignationsViewABC(
    AssignationsViewFeatureABC,
    View,
    ModelObserverMixin[ModelT],
    ABC,
):
    """Abstract base class for Assigned exercise page."""


class AssignationsViewObserver(
    ABC,
):
    """Abstract base class for assigned view event observer."""

    @abstractmethod
    def exercise_selected(self, value: str) -> None:
        """Handle exercise selected event."""


# Controller


class AssignationsControllerABC(
    AssignationsModelObserver,
    AssignationsViewObserver,
    PageControllerABC[ViewT],
    ABC,
):
    """Abstract base class for Assigned exercises page."""
