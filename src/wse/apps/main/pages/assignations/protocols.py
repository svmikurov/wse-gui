"""Defines protocols and ABC for Assigned exercises page."""

from typing import Any, Protocol

from wse.apps.main.api.schema import ExerciseInfo, ExerciseMeta
from wse.feature.interfaces.imvc import (
    ModelProto,
    PageControllerProto,
    ViewProto,
)

# Model


class AssignationsModelFeatureProto(Protocol):
    """Protocol for assigned page model feature interface."""

    def fetch_exercises(self) -> None:
        """Fetch assigned exercises."""

    def fetch_exercise(
        self,
        assignation_id: str,
    ) -> ExerciseMeta | None:
        """Fetch assigned exercise meta data."""


class AssignationsModelProto(
    AssignationsModelFeatureProto,
    ModelProto,
    Protocol,
):
    """Protocol for Assigned exercises page model interface."""


class AssignationsModelObserveProto(Protocol):
    """Protocol for assigned model event observer interface."""

    def exercises_updated(self, exercises: list[ExerciseInfo]) -> None:
        """Update view on update exercises event."""


# View


class AssignationsViewFeatureProto(Protocol):
    """Protocol for assigned view feature interface."""

    def update_exercises(self, exercises: list[ExerciseInfo]) -> None:
        """Update exercises to display."""

    def exercise_selected(self, value: str) -> None:
        """Notify that the exercise has been selected."""


class AssignationsViewProto(
    AssignationsViewFeatureProto,
    ViewProto,
    Protocol,
):
    """Protocol for Assigned exercise page view interface."""


class AssignationsViewObserveProto(Protocol):
    """Protocol for assigned view event observer interface."""

    def exercise_selected(self, exercise_id: str) -> None:
        """Handle exercise selected event."""


# Controller


class AssignationsControllerProto(
    AssignationsModelObserveProto,
    AssignationsViewObserveProto,
    PageControllerProto[Any],
    Protocol,
):
    """Protocol for Assigned exercises page controller interface."""
