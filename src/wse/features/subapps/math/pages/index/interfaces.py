"""Defines protocols for Main Math page components interface."""

from typing import Protocol

from wse_exercises.core.mathem.enums import Exercises

from wse.features.interfaces import IView
from wse.features.interfaces.imvc import IModel, IPageController


class IIndexMathModel(
    IModel,
    Protocol,
):
    """Protocol for Main Math page model interface."""

    def on_open(self) -> None:
        """Call methods when page opens."""

    def change_exersice(self, value: Exercises) -> None:
        """Change the exercise to perform."""

    def start_exercise(self) -> None:
        """Handle the event to start exercise."""


class IIndexMathView(
    IView,
    Protocol,
):
    """Protocol for Main Math page view interface."""

    def update_exercise_selection(self, exercises: list[Exercises]) -> None:
        """Update the Exercise selection data source."""


class IIndexMathController(
    IPageController,
    Protocol,
):
    """Protocol for Main Math page controller interface."""

    # Notifications from Model

    def exercises_updated(self, values: list[Exercises]) -> None:
        """Update exercises selection data source."""

    def exercise_started(self, value: Exercises) -> None:
        """Navigate to exercise page."""

    # Notifications from view

    def exercise_changed(self, value: Exercises) -> None:
        """Handle the change of exercise type."""

    def start_button_pressed(self) -> None:
        """Handle the start exercise button pressed."""
