"""Defines exercise service."""

from injector import inject

from wse.api.main import AssignedApiABC
from wse.api.math.abc import CalculationApiABC
from wse.api.math.schemas import Calculation
from wse.api.schemas.exercise import Assigned

from .base import ExerciseService


class CalculationService(
    ExerciseService[Calculation],
):
    """Simple math calculation exercise service."""

    @inject
    def __init__(
        self,
        exercise_api: CalculationApiABC,
    ) -> None:
        """Construct the exercise."""
        super().__init__(exercise_api)


class AssignedService(
    ExerciseService[Assigned],
):
    """Assigned exercise service."""

    @inject
    def __init__(
        self,
        exercise_api: AssignedApiABC,
    ) -> None:
        """Construct the exercise."""
        super().__init__(exercise_api)
