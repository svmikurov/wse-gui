"""Defines API for exercises."""

import logging
from typing import Any

from injector import inject
from typing_extensions import override

from wse.core.http import IHttpClient
from wse.core.interfaces.iapi import IAuthScheme

from .config import ExercisesApiConfig
from .dto import AssignedExerciseDTO
from .iapi import AssignedExercisesABC

logger = logging.getLogger(__name__)


class AssignedExercisesApi(AssignedExercisesABC):
    """Protocol for assigned exercises API interface."""

    @inject
    def __init__(
        self,
        http_client: IHttpClient,
        auth_scheme: IAuthScheme,
        api_config: ExercisesApiConfig,
    ) -> None:
        """Construct the API."""
        self._http_client = http_client
        self._auth_scheme = auth_scheme
        self._api_config = api_config

    @override
    def request_all_exercises(self) -> list[AssignedExerciseDTO]:
        """Request all assigned by mentors exercises."""
        try:
            response = self._http_client.get(
                url=self._api_config.assigned_exercises,
                auth=self._auth_scheme,
            )
        except Exception as e:
            logger.exception(f'Request all assigned exercises error: {str(e)}')
            raise e
        else:
            return self._create_assigned_exercises_dtos(response.json())

    @staticmethod
    def _create_assigned_exercises_dtos(
        response_data: list[dict[str, Any]],
    ) -> list[AssignedExerciseDTO]:
        exercises: list[AssignedExerciseDTO] = []
        for data in response_data:
            exercises.append(AssignedExerciseDTO(**data))
        return exercises
