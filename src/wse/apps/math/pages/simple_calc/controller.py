"""Defines the controller of Simple Math Calculation page."""

from dataclasses import dataclass
from typing import Any

from injector import inject

from wse.features.base.mvc import BasePageController

from .interfaces import (
    ICalcModel,
    ICalcView,
)


@inject
@dataclass
class CalcController(
    BasePageController,
):
    """The controller of Simple Math calculation page."""

    _model: ICalcModel
    _view: ICalcView

    def _setup(self) -> None:
        """Set up the controller features."""
        self._model.add_observer(self)

    # TODO: Fix noqa: ANN401
    def on_open(self, **kwargs: Any) -> None:  # noqa: ANN401
        """Call controller methods when page opens."""
        self._model.on_open(kwargs['exercise'])
        self._view.reset_layout()

    # Notifications from Model

    def question_updated(self, value: str) -> None:
        """Display the question."""
        self._view.display_question(value)

    def question_cleared(self) -> None:
        """Clear the question text."""
        self._view.clear_question()

    def answer_updated(self, value: str) -> None:
        """Display the user answer."""
        self._view.display_answer(value)

    def answer_cleared(self) -> None:
        """Clear the question text."""
        self._view.clear_answer()

    def correct_answer_received(self, value: str) -> None:
        """Display the correct answer."""
        self._view.display_correct_answer(value)

    # Notifications from View

    def numpad_input_updated(self, value: str) -> None:
        """Update user input for model."""
        self._model.handle_answer_input(value)

    def answer_confirmed(self) -> None:
        """Handle the task submit event."""
        self._model.handle_submit()

    def task_started(self) -> None:
        """Handle the next task started event."""
        self._model.start_new_task()
