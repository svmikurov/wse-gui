"""Exercise assignations API client."""

import logging
from typing import Any

import httpx
from injector import inject
from pydantic import ValidationError
from typing_extensions import override

from wse.config.api import APIConfigV1
from wse.core.http import AuthSchemaABC, HttpClientABC
from wse.data.schemas.exercise import Assigned, ExerciseInfo

from . import AssignationsApiABC

log = logging.getLogger(__name__)


class AssignationsApi(AssignationsApiABC):
    """Exercise assignations API client."""

    @inject
    def __init__(
        self,
        http_client: HttpClientABC,
        auth_scheme: AuthSchemaABC,
        api_config: APIConfigV1,
    ) -> None:
        """Construct the API."""
        self._http_client = http_client
        self._auth = auth_scheme
        self._api = api_config

    @override
    def request_all_exercises(self) -> list[ExerciseInfo] | None:
        """Request all assigned by mentors exercises."""
        try:
            response = self._http_client.get(
                url=self._api.assigned_exercises,
                auth=self._auth,
            )
            log.debug('Assigned exercises updated')

        except httpx.HTTPError:
            log.error('Request all assigned exercises error')
            return None

        else:
            try:
                return self._collect(response.json())
            except ValidationError:
                log.exception('Question validation error')
                return None

    @override
    def request_selected(self, assignation_id: str) -> Assigned | None:
        """Request selected exercise."""
        try:
            response = self._http_client.get(
                url=self._api.selected_exercise.format(
                    assignation_id=assignation_id,
                ),
                auth=self._auth,
            )

        except httpx.HTTPError:
            log.exception('Assigned exercise request error')
            return None

        else:
            try:
                assigned_exercise = Assigned(**response.json())
            except ValidationError as e:
                log.exception(f'Create Exercise meta error: {str(e)}')
                return None
            else:
                return assigned_exercise

    @staticmethod
    def _collect(
        response_data: list[dict[str, Any]],
    ) -> list[ExerciseInfo]:
        exercises: list[ExerciseInfo] = []
        for data in response_data:
            exercises.append(ExerciseInfo(**data))
        return exercises
