"""Calculation exercise Use Cases."""

from injector import inject
from wse_exercises.core import MathEnum

from ..data.repositories.calculation_exercises import CalculationExerciseRepo


class SetCalculationExerciseUseCase:
    """Use Case for set current Calculation exercise."""

    @inject
    def __init__(self, repository: CalculationExerciseRepo) -> None:
        """Construct the case."""
        self._repository = repository

    def set_default(self, exercise: MathEnum) -> None:
        """Set Calculation exercise as default."""
        self._repository.set_default(exercise)
