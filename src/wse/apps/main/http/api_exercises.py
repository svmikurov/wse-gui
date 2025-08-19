"""Defines API for exercises."""

import logging
from typing import Any

from injector import inject
from pydantic import ValidationError
from typing_extensions import override

from wse.config.api_paths import APIConfigV1
from wse.core.http import IHttpClient
from wse.core.interfaces.iapi import IAuthScheme

from .dto import AssignedExerciseDTO, ExerciseMetaDTO
from .iapi import AssignedExercisesABC

logger = logging.getLogger(__name__)


class AssignedExercisesApi(AssignedExercisesABC):
    """Protocol for assigned exercises API interface."""

    @inject
    def __init__(
        self,
        http_client: IHttpClient,
        auth_scheme: IAuthScheme,
        api_config: APIConfigV1,
    ) -> None:
        """Construct the API."""
        self._http_client = http_client
        self._auth = auth_scheme
        self._api = api_config

    @override
    def request_all_exercises(self) -> list[AssignedExerciseDTO] | None:
        """Request all assigned by mentors exercises."""
        try:
            response = self._http_client.get(
                url=self._api.assigned_exercises,
                auth=self._auth,
            )

        except Exception:
            logger.error('Request all assigned exercises error')
            return None

        else:
            return self._create_assigned_exercises_dtos(response.json())

    @override
    def request_selected(self, assignation_id: str) -> ExerciseMetaDTO | None:
        """Request selected exercise."""
        try:
            response = self._http_client.get(
                url=self._api.selected_exercise.format(
                    assignation_id=assignation_id,
                ),
                auth=self._auth,
            )

        except Exception:
            logger.exception('Assigned exercise request error')
            return None

        else:
            try:
                dto = ExerciseMetaDTO(**response.json())
            except ValidationError as e:
                logger.exception(f'Create Exercise meta DTO error: {str(e)}')
                return None
            else:
                return dto

    @staticmethod
    def _create_assigned_exercises_dtos(
        response_data: list[dict[str, Any]],
    ) -> list[AssignedExerciseDTO]:
        exercises: list[AssignedExerciseDTO] = []
        for data in response_data:
            exercises.append(AssignedExerciseDTO(**data))
        return exercises
