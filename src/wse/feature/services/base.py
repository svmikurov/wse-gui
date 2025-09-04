"""Base exercise service."""

from typing import TypeVar

from wse.apps.main.api.schema import ExerciseMeta
from wse.core.api import (
    ExerciseApiProto,
    RelatedData,
)

from . import Answer, Question, Result
from .abc import BaseExerciseService

ExerciseT = TypeVar(
    'ExerciseT',
    bound=ExerciseMeta,
)


class ExerciseService(
    BaseExerciseService[ExerciseT],
):
    """Exercise service."""

    def __init__(
        self,
        api_client: ExerciseApiProto[ExerciseT],
    ) -> None:
        """Construct the service."""
        self._api_client = api_client

    def get_task(
        self,
        exercise: ExerciseT,
    ) -> tuple[Question, RelatedData | None] | tuple[None, None]:
        """Get task."""
        if response := self._api_client.request_task(exercise):
            return response.data, response.related_data
        return None, None

    def check_answer(
        self,
        answer: Answer,
        exercise: ExerciseT,
    ) -> tuple[Result, RelatedData | None] | tuple[None, None]:
        """Check the user answer."""
        if response := self._api_client.check_answer(answer, exercise):
            return response.data, response.related_data
        return None, None
