"""Calculation exercise data source."""

from typing import Literal

from wse.data.entities.exercise import CalculationExercise

_NotifyT = Literal['']


class CalculationExerciseSource:
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
