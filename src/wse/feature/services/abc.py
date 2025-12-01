"""Abstract base class for services."""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from wse.api.responses import RelatedData
from wse.data.schemas.exercise import ExerciseMeta
from wse.data.schemas.task import Answer, Question, Result

ExerciseT = TypeVar('ExerciseT', bound=ExerciseMeta)


class ExerciseServiceABC(
    ABC,
    Generic[ExerciseT],
):
    """Abstract base class for Exercise service."""

    @abstractmethod
    def get_task(
        self,
        exercise: ExerciseT,
    ) -> tuple[Question, RelatedData | None] | tuple[None, None]:
        """Get task."""

    @abstractmethod
    def check_answer(
        self,
        answer: Answer,
        exercise: ExerciseT,
    ) -> tuple[Result, RelatedData | None] | tuple[None, None]:
        """Check the user answer."""
