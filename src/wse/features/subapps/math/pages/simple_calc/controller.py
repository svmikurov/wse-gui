"""Defines the controller of Simple Math Calculation page."""

from dataclasses import dataclass

from injector import inject
from typing_extensions import override

from wse.features.base.mvc import BasePageController
from wse.features.interfaces import IContent

from .interfaces import ISimpleCalcModel, ISimpleCalcView


@inject
@dataclass
class SimpleCalcController(BasePageController):
    """The controller of Simple Math calculation page."""

    _model: ISimpleCalcModel
    _view: ISimpleCalcView

    def _setup(self) -> None:
        """Set up the controller features."""
        self._model.add_observer(self)

    def _on_open(self) -> None:
        """Call controller methods when page opens."""
        self._model.on_open()

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

    # Notifications from View

    def numpad_input_updated(self, value: str) -> None:
        """Update user input for model."""
        self._model.handle_answer_input(value)

    def answer_confirmed(self) -> None:
        """Handle the user's confirmation of the entered answer."""
        self._model.check_answer()

    # Properties

    @override
    @property
    def content(self) -> IContent:
        """Add haling of page open event."""
        self._on_open()
        return super().content
