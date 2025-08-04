"""Defines protocols for Simple Math Calculation page components."""

from typing import Protocol

from wse_exercises.base.enums import ExerciseEnum

from wse.features.interfaces.imvc import IModel, IPageController, IView


class ICalcModel(
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


class ICalcView(
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


class ICalcController(
    IPageController,
    Protocol,
):
    """The controller of Simple Math calculation page."""

    _model: ICalcModel
    _view: ICalcView

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
