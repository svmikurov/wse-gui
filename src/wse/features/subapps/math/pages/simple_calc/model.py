"""Defines Simple Math calculation page model."""

from dataclasses import dataclass

from injector import inject
from typing_extensions import override

from wse.features.base.mvc import BaseModel
from wse.features.services.interfaces import IExerciseService


@inject
@dataclass
class SimpleCalcModel(
    BaseModel,
):
    """Simple Math calculation page model."""

    _exercise: IExerciseService

    @override
    def _setup(self) -> None:
        self._exercise.add_observer(self)

    # Notifications about Model events

    def _display_question(self) -> None:
        self._subject.notify('question_updated', value='1 + 1')

    def _clear_question(self) -> None:
        self._subject.notify('question_cleared')

    def _display_answer(self, value: str) -> None:
        self._subject.notify('answer_updated', value=value)

    def _clear_answer(self) -> None:
        self._subject.notify('answer_cleared')

    # API for controller

    def on_open(self) -> None:
        """Call model methods when page opens."""
        self._display_question()

    def handle_answer_input(self, value: str) -> None:
        """Handel the user answer input."""
        self._display_answer(value)

    def check_answer(self) -> None:
        """Check the user's confirmed answer."""
        pass
