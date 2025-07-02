"""Defines Index Math page model."""

from dataclasses import dataclass

from injector import inject
from typing_extensions import override
from wse_exercises.core.mathem.enums import Exercises

from wse.features.base import BaseModel
from wse.features.subapps.math.pages.index.interfaces import IIndexMathModel


@inject
@dataclass
class IndexMathModel(
    BaseModel,
    IIndexMathModel,
):
    """Index Math page model."""

    _exercises: list[Exercises]

    @override
    def __post_init__(self) -> None:
        """Construct the model."""
        super().__post_init__()
        self._default_exercise: Exercises = Exercises.ADDING
        self._current_exercise: Exercises = self._default_exercise

    # Notifications about Self events

    def _notify_exercises_updated(self) -> None:
        self._notify('exercises_updated', values=self._exercises)

    def _notify_start_exercise(self, value: Exercises) -> None:
        self._notify('exercise_started', value=value)

    # Api for controller

    @override
    def on_open(self) -> None:
        """Call methods when page opens."""
        self._notify_exercises_updated()

    @override
    def change_exersice(self, value: Exercises) -> None:
        """Change the exercise to perform."""
        self._current_exercise = value

    @override
    def start_exercise(self) -> None:
        """Handle the event to start exercise."""
        self._notify_start_exercise(value=self._current_exercise)
