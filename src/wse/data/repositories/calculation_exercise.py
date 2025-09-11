"""Calculation exercise repository."""

from dataclasses import dataclass

from injector import inject
from wse_exercises.core import MathEnum

from ..sources.exercise import CalculationExerciseSource


@inject
@dataclass
class CalculationExerciseRepo:
    """Calculation exercise repository."""

    _calculation_exercise_source: CalculationExerciseSource

    def set_default(self, exercise: MathEnum) -> None:
        """Set Calculation exercise as default."""
        self._calculation_exercise_source.set_default(exercise)

    @property
    def default(self) -> MathEnum:
        """Get default calculation exercise."""
        return self._calculation_exercise_source.data.default

    @property
    def exercises(self) -> list[MathEnum]:
        """Get available calculation exercise enumeration."""
        return self._calculation_exercise_source.data.exercises
