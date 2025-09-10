"""Calculation exercise repository."""
from dataclasses import dataclass

from injector import inject

from ..sources.exercise import CalculationExerciseSource


@inject
@dataclass
class CalculationExerciseRepository:
    """Calculation exercise repository."""

    _calculation_exercise_source: CalculationExerciseSource

    @property
    def exercise(self) -> str:
        """Get calculation exercise."""
        return self._calculation_exercise_source.data.name
