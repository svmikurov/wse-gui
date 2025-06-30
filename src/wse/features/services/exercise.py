"""Defines exercise service."""

import logging

from injector import inject
from wse_exercises.core.mathem.interfaces import (
    ISimpleCalcTask,
)
from wse_exercises.core.mathem.task import SimpleMathTask

from ...core.api.interfaces import IExerciseApi
from ...core.interfaces.iauth import IAuthService
from ..base.mixins import AddObserverMixin

logger = logging.getLogger(__name__)


@inject
class SimpleCalcService(
    AddObserverMixin,
):
    """Simple math calculation exercise service."""

    def __init__(
        self,
        auth_service: IAuthService,
        exercise_api: IExerciseApi,
    ) -> None:
        """Construct the exercise."""
        self._auth_service = auth_service
        self._exercise_api = exercise_api

    def get_task(self) -> ISimpleCalcTask:
        """Get task."""
        task_data = self._exercise_api.request_task()
        task_dto = SimpleMathTask.from_dict(task_data)
        return task_dto

    @classmethod
    def check_answer(
        cls,
        user_answer: str,
        task: ISimpleCalcTask,
    ) -> bool:
        """Check the user answer."""
        return bool(user_answer == task.answer.text)
