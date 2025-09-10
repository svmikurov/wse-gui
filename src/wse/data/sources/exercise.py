"""Exercise data source."""

from typing import Literal

from wse.data.entities.exercise import CalculationExercise

_NotifyT = Literal['']


class DivisionExerciseSource:
    """Exercise data source."""

    def __init__(self) -> None:
        """Construct the source."""
        super().__init__()
        # This is the single source of troth.
        self._exercise = CalculationExercise()

    @property
    def data(self) -> CalculationExercise:
        """Exercise source data."""
        return self._exercise
