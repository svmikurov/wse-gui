"""Defines protocols for Simple Math Calculation page components."""

from typing import Protocol

from wse_exercises.base.enums import ExerciseEnum

from wse.config.layout import TextTaskStyle, TextTaskTheme
from wse.features.interfaces import (
    IGetContent,
    IModel,
    IPageController,
    IView,
)


class ISimpleCalcModel(
    IModel,
    Protocol,
):
    """Simple math calculation page view."""

    def start_new_task(self) -> None:
        """Start new task."""

    # API for controller

    def on_open(self, exercise: ExerciseEnum) -> None:
        """Call model methods when page opens."""

    def handle_answer_input(self, value: str) -> None:
        """Handel the user answer input."""

    def handle_submit(self) -> None:
        """Check the user's confirmed answer."""

    # Properties

    @property
    def current_exercise(self) -> ExerciseEnum | None:
        """Current exercise to do."""

    @current_exercise.setter
    def current_exercise(self, value: ExerciseEnum) -> None: ...


class ISimpleCalcView(
    IView,
    Protocol,
):
    """Simple math calculation page view."""

    # Notifications from NumPad

    def numpad_input_updated(self, value: str) -> None:
        """Update user input."""

    # API for controller

    def display_question(self, value: str) -> None:
        """Display the question."""

    def clear_question(self) -> None:
        """Clear the question text."""

    def display_answer(self, value: str) -> None:
        """Display the user answer."""

    def clear_answer(self) -> None:
        """Clear the answer text."""

    def display_correct_answer(self, value: str) -> None:
        """Display the correct answer."""

    def reset_layout(self) -> None:
        """Reset to initial layout."""


class ISimpleCalcController(
    IPageController,
    Protocol,
):
    """The controller of Simple Math calculation page."""

    _model: ISimpleCalcModel
    _view: ISimpleCalcView

    # Notifications from Model

    def question_updated(self, value: str) -> None:
        """Display the question."""
        self._view.display_question(value)

    def question_cleared(self) -> None:
        """Clear the question text."""
        self._view.clear_question()

    def answer_updated(self, value: str) -> None:
        """Display the user answer."""

    def answer_cleared(self) -> None:
        """Clear the question text."""

    # Notifications from View

    def numpad_input_updated(self, value: str) -> None:
        """Update user input for model."""
        self._model.handle_answer_input(value)

    def answer_confirmed(self) -> None:
        """Handle the task submit event."""

    def task_started(self) -> None:
        """Handle the next task started event."""


class ISimpleCalcContainer(
    IGetContent,
    Protocol,
):
    """Protocol fot Simple Math calculation container interface."""

    # Layout methods

    def localize_ui(self) -> None:
        """Localize the UI text."""

    def update_style(self, config: TextTaskStyle | TextTaskTheme) -> None:
        """Update widgets style."""

    # API for view

    def display_output(self, value: str) -> None:
        """Update the output text field."""

    def clear_output(self) -> None:
        """Clear the output text field."""

    def display_input(self, value: str) -> None:
        """Update the input text field."""

    def clear_input(self) -> None:
        """Clear the input text field."""
