"""Defines protocols for Main Math page components interface."""

from typing import Protocol

from wse_exercises.base.enums import ExerciseEnum

from wse.features.interfaces.imvc import IModel, IPageController, IView
from wse.features.shared.containers.iabc.itop_bar import ITopBarPageViewMixin


class IIndexMathModel(
    IModel,
    Protocol,
):
    """Protocol for Main Math page model interface."""

    def on_open(self) -> None:
        """Call methods when page opens."""

    def change_exersice(self, value: ExerciseEnum) -> None:
        """Change the exercise to perform."""

    def start_exercise(self) -> None:
        """Handle the event to start exercise."""


class IIndexMathView(
    ITopBarPageViewMixin,
    IView,
    Protocol,
):
    """Protocol for Main Math page view interface."""

    def update_exercise_selection(self, exercises: list[ExerciseEnum]) -> None:
        """Update the Exercise selection data source."""

    def set_selected_exercise(self, value: ExerciseEnum) -> None:
        """Set selected exercise to choices."""


class IIndexMathController(
    IPageController,
    Protocol,
):
    """Protocol for Main Math page controller interface."""

    # Notifications from Model

    def exercises_updated(self, values: list[ExerciseEnum]) -> None:
        """Update exercises selection data source."""

    def exercise_started(self, value: ExerciseEnum) -> None:
        """Navigate to exercise page."""

    def exercise_selected(self, value: ExerciseEnum) -> None:
        """Set selected exercise to choices."""

    # Notifications from view

    def exercise_changed(self, value: ExerciseEnum) -> None:
        """Handle the change of exercise type."""

    def start_button_pressed(self) -> None:
        """Handle the start exercise button pressed."""
