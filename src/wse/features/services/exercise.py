"""Defines exercise service."""

import logging
import uuid
from typing import Any, final

from injector import inject
from typing_extensions import override

from wse.apps.math.pages.simple_calc.dto import (
    CalcAnswerDTO,
    CalcResultDTO,
    CalcTaskDTO,
)
from wse.core.exceptions import ExerciseError
from wse.core.interfaces.iapi import IExerciseApiClient

from ..base.mixins import AddObserverMixin
from .interfaces import ICalcService

logger = logging.getLogger(__name__)


@final
class CalcService(AddObserverMixin, ICalcService):
    """Simple math calculation exercise service."""

    @inject
    def __init__(
        self,
        exercise_api: IExerciseApiClient,
    ) -> None:
        """Construct the exercise."""
        self._exercise_api = exercise_api
        # The service uses the task UID in requests to
        # check the answer to a specific task by its UID.
        self._task_uid: uuid.UUID | None = None

    @override
    def get_task(self, data: dict[str, Any]) -> CalcTaskDTO:
        """Get task.

        Gets a task from the server using the Exercise API client.
        """
        request_data = self._exercise_api.request_task(data)
        response_dto = CalcTaskDTO.from_dict(request_data)
        self._task_uid = response_dto.uid
        return response_dto

    @override
    def check_answer(self, user_answer: str) -> CalcResultDTO:
        """Check user answer.

        Checks the user's answer on the server using the Exercise API
        client.
        """
        if self._task_uid is None:
            raise ExerciseError('Task UID is not defined')

        answer_dto = CalcAnswerDTO(uid=self._task_uid, answer=user_answer)

        try:
            result_dto = self._exercise_api.check_answer(answer_dto)

        except ExerciseError:
            logger.exception('Answer check failed')
            raise

        if result_dto.is_correct:
            self._task_uid = None

        return result_dto
