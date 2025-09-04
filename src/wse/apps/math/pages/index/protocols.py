"""Defines protocols for Main Math page components interface."""

from typing import Protocol, TypeVar

from wse_exercises.base.enums import ExerciseEnum

from wse.apps.math.api import Calculation
from wse.feature.interfaces.imvc import (
    ModelProto,
    PageControllerProto,
    ViewProto,
)
from wse.feature.shared.containers.top_bar.itop_bar import (
    TopBarViewMixinProto,
)

T_contra = TypeVar('T_contra', contravariant=True)


# Model


class MathModelFeatureProto(Protocol):
    """Protocol for Index Math model feature interface."""

    def update_page_context(self) -> None:
        """Update page content."""

    def change_exercise(self, value: ExerciseEnum) -> None:
        """Change the exercise to perform."""

    def start_exercise(self) -> None:
        """Handle the event to start exercise."""


class MathModelProto(
    ModelProto,
    MathModelFeatureProto,
    Protocol,
):
    """Protocol for Main Math page model interface."""


class MathModelObserverProto(Protocol):
    """Protocol for Index Math page model observer interface."""

    def exercises_updated(self, values: list[ExerciseEnum]) -> None:
        """Update exercises select data source."""

    def exercise_started(self, value: Calculation) -> None:
        """Navigate to exercise page."""

    def exercise_selected(self, value: ExerciseEnum) -> None:
        """Set selected exercise to choices."""


# View


class MathViewProto(
    TopBarViewMixinProto,
    ViewProto,
    Protocol,
):
    """Protocol for Main Math page view interface."""

    def update_exercise_select(self, exercises: list[ExerciseEnum]) -> None:
        """Update the Exercise select data source."""

    def set_selected_exercise(self, value: ExerciseEnum) -> None:
        """Set selected exercise to choices."""


class MathViewObserverProto(Protocol):
    """Protocol for Index Math page view observer interface."""

    def exercise_changed(self, value: ExerciseEnum) -> None:
        """Handle the change of exercise type."""

    def start_button_pressed(self) -> None:
        """Handle the start exercise button pressed."""


# Controller


class MathControllerProto(
    PageControllerProto[T_contra],
    Protocol,
):
    """Protocol for Index Math page controller interface."""
