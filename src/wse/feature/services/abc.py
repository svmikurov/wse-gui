"""Abstract base class for services."""

from abc import ABC, abstractmethod
from typing import TypeVar

from wse.apps.main.api.schema import ExerciseMeta
from wse.core.api.response import RelatedData

from . import Answer, ExerciseServiceProto, Question, Result

ExerciseT = TypeVar(
    'ExerciseT',
    bound=ExerciseMeta,
)


class BaseExerciseService(
    ABC,
    ExerciseServiceProto[ExerciseT],
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
