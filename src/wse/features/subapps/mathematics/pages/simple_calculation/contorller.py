"""Defines the controller of Simple Math calculation page."""

from dataclasses import dataclass

from injector import inject

from wse.features.base import BaseController

from .interfaces import ISimpleCalcModel, ISimpleCalcView


@inject
@dataclass
class SimpleCalcController(BaseController):
    """The controller of Simple Math calculation page."""

    _model: ISimpleCalcModel
    _view: ISimpleCalcView

    def _setup(self) -> None:
        """Set up the controller features."""
        self._model.add_observer(self)
        self._view.subscribe_to_numpad(self)

    # Model event notifications

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

    # NumPad event notifications

    def numpad_input_updated(self, value: str) -> None:
        """Update user input for model."""
        self._model.handle_input_updated(value)
