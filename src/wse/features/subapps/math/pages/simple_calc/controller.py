"""Defines the controller of Simple Math Calculation page."""

from dataclasses import dataclass
from typing import Any

from injector import inject
from typing_extensions import override

from wse.features.base.mvc import BasePageController

from .interfaces import (
    ISimpleCalcController,
    ISimpleCalcModel,
    ISimpleCalcView,
)


@inject
@dataclass
class SimpleCalcController(
    BasePageController,
    ISimpleCalcController,
):
    """The controller of Simple Math calculation page."""

    _model: ISimpleCalcModel
    _view: ISimpleCalcView

    @override
    def _setup(self) -> None:
        """Set up the controller features."""
        self._model.add_observer(self)

    @override
    def on_open(self, **kwargs: Any) -> None:
        """Call controller methods when page opens."""
        self._model.on_open(kwargs['exercise'])

    # Notifications from Model

    @override
    def question_updated(self, value: str) -> None:
        """Display the question."""
        self._view.display_question(value)

    @override
    def question_cleared(self) -> None:
        """Clear the question text."""
        self._view.clear_question()

    @override
    def answer_updated(self, value: str) -> None:
        """Display the user answer."""
        self._view.display_answer(value)

    @override
    def answer_cleared(self) -> None:
        """Clear the question text."""
        self._view.clear_answer()

    # Notifications from View

    @override
    def numpad_input_updated(self, value: str) -> None:
        """Update user input for model."""
        self._model.handle_answer_input(value)

    @override
    def answer_confirmed(self) -> None:
        """Handle the task submit event."""
        self._model.handle_submit()
