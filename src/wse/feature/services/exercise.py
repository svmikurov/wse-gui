"""Defines exercise service."""

from injector import inject

from wse.feature.api.main import AssignedApiProto
from wse.feature.api.math import Calculation
from wse.feature.shared.schemas.exercise import Assigned

from ..api.math.protocol import CalculationApiProto
from .base import ExerciseService


class CalculationService(
    ExerciseService[Calculation],
):
    """Simple math calculation exercise service."""

    @inject
    def __init__(
        self,
        exercise_api: CalculationApiProto,
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
        exercise_api: AssignedApiProto,
    ) -> None:
        """Construct the exercise."""
        super().__init__(exercise_api)
