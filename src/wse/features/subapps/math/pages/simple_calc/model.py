"""Defines Simple Math calculation page model."""

from dataclasses import dataclass

from injector import inject

from wse.features.base.mvc import BaseModel
from wse.features.services.interfaces import IExerciseService


@inject
@dataclass
class SimpleCalcModel(BaseModel):
    """Simple Math calculation page model."""

    _exercise: IExerciseService

    def _setup(self) -> None:
        self._exercise.add_observer(self)

    # Event notification

    def answer_updated(self, value: str) -> None:
        """Handle the user answer update."""
        self._subject.notify('answer_updated', value=value)

    # API for controller

    def handle_input_updated(self, value: str) -> None:
        """Handle the user input symbol."""
        self._exercise.update_answer(value)
