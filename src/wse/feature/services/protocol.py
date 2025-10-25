"""Protocol for exercise service interface."""

from typing import Protocol, TypeVar

from wse.api.math import Calculation
from wse.api.schemas.exercise import Assigned
from wse.api.schemas.task import Answer, Question, Result
from wse.core.api.response import RelatedData

ExerciseT = TypeVar('ExerciseT', contravariant=True)


class ExerciseServiceProto(
    Protocol[ExerciseT],
):
    """Generic protocol for exercise service."""

    def get_task(
        self,
        exercise: ExerciseT,
    ) -> tuple[Question, RelatedData | None] | tuple[None, None]:
        """Get task."""

    def check_answer(
        self,
        answer: Answer,
        exercise: ExerciseT,
    ) -> tuple[Result, RelatedData | None] | tuple[None, None]:
        """Check the user answer."""


class AssignedServiceProto(
    ExerciseServiceProto[Assigned],
    Protocol,
):
    """Protocols for Assigned exercise service interface."""


class CalculationServiceProto(
    ExerciseServiceProto[Calculation],
    Protocol,
):
    """Protocols for Exercise Service interface."""
