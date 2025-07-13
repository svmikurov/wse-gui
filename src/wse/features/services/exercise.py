"""Defines exercise service."""

import logging

from injector import inject
from typing_extensions import override
from wse_exercises.base.components import TextAnswer
from wse_exercises.base.enums import ExerciseEnum
from wse_exercises.core.math.rest import SimpleCalcAnswer, SimpleCalcResponse
from wse_exercises.core.math.task import SimpleCalcTask

from wse.core.exceptions import ExerciseError
from wse.core.interfaces.iapi import IExerciseAPI

from ..base.mixins import AddObserverMixin
from .interfaces import ISimpleCalcService

logger = logging.getLogger(__name__)


class SimpleCalcService(AddObserverMixin, ISimpleCalcService):
    """Simple math calculation exercise service."""

    @inject
    def __init__(
        self,
        exercise_api: IExerciseAPI,
    ) -> None:
        """Construct the exercise."""
        self._exercise_api = exercise_api
        # The service uses the task UID in requests to
        # check the answer to a specific task by its UID.
        self._task_uid: str | None = None

    @override
    def get_task(self, exercise: ExerciseEnum) -> SimpleCalcTask:
        """Get task."""
        request_dto = self._exercise_api.request_task(exercise)
        response_dto = SimpleCalcResponse.from_dict(request_dto)
        self._task_uid = response_dto.uid
        return response_dto.task

    @override
    def check_answer(self, user_answer: str) -> bool:
        """Check the user answer."""
        if self._task_uid is None:
            raise ExerciseError('Unique task identifier is not defined')

        answer_dto = SimpleCalcAnswer(
            uid=self._task_uid,
            answer=TextAnswer(text=user_answer),
        )

        try:
            is_correct = self._exercise_api.check_answer(answer_dto)

        except ExerciseError as e:
            logger.exception(f'Answer check error: {e}')
            raise

        else:
            if is_correct:
                self._task_uid = None
            return is_correct
