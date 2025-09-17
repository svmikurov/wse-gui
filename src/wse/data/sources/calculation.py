"""Calculation exercise data source."""

from abc import ABC, abstractmethod
from dataclasses import replace
from typing import Literal

from wse_exercises.core import MathEnum

from wse.data.entities.exercise import CalculationExercise
from wse.data.sources.base.source import DataSourceGen

_NotifyT = Literal['default_updated']


class ExerciseObserverABC(ABC):
    """ABC for task source observer."""

    @abstractmethod
    def default_updated(self, default: MathEnum) -> None:
        """Handle the 'default updated' Exercise source event."""


class CalculationExerciseSource(
    DataSourceGen[
        ExerciseObserverABC,
        _NotifyT,
    ]
):
    """Calculation exercise data source."""

    def __init__(self) -> None:
        """Construct the source."""
        super().__init__()
        # This is the single source of troth.
        self._exercise = CalculationExercise()

    @property
    def data(self) -> CalculationExercise:
        """Calculation exercise source data."""
        return self._exercise

    def set_default(self, exercise: MathEnum) -> None:
        """Set Calculation exercise as default."""
        self._exercise = replace(self._exercise, default=exercise)
        self.notify('default_updated', default=exercise)
