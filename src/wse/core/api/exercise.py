"""Defines exercise API."""

import logging
from typing import Any, cast

import httpx
from httpx import Response
from injector import inject
from typing_extensions import override
from wse_exercises.base.enums import ExerciseEnum
from wse_exercises.core.math.rest import SimpleCalcAnswer

from wse.config.settings import APIConfigV1
from wse.core.exceptions import ExerciseError
from wse.core.interfaces.iapi import IAuthScheme, IExerciseAPI, IHttpClient

logger = logging.getLogger(__name__)


@inject
class ExerciseAPI(IExerciseAPI):
    """Exercise API."""

    def __init__(
        self,
        auth_scheme: IAuthScheme,
        http_client: IHttpClient,
        api_config: APIConfigV1,
    ) -> None:
        """Construct the API."""
        self._auth_scheme = auth_scheme
        self._http_client = http_client
        # Endpoints
        self._get_task_endpoint = api_config.task['get_task']
        self._validate_answer_endpoint = api_config.task['validate_answer']

    @override
    def request_task(self, exercise: ExerciseEnum) -> dict[str, Any]:
        """Request the task."""
        data = {
            'name': exercise,
            'config': {'min_value': '1', 'max_value': '9'},
        }
        try:
            response: Response = self._http_client.post(
                url=self._get_task_endpoint,
                json=data,
                auth=cast(httpx.Auth, self._auth_scheme),
            )
        except Exception as e:
            logger.error('Request task error: %s', str(e))
            raise ExerciseError from e

        response_data: dict[str, Any] = response.json()
        return response_data

    @override
    def check_answer(self, answer: SimpleCalcAnswer) -> bool:
        """Check the user entered answer."""
        try:
            response: Response = self._http_client.post(
                url=self._validate_answer_endpoint,
                json=answer.to_dict(),
                auth=cast(httpx.Auth, self._auth_scheme),
            )

        except httpx.HTTPStatusError:
            logger.error('Http client error')
            raise

        else:
            try:
                is_correct: bool = response.json().get('is_correct')
            except AttributeError as e:
                raise ExerciseError from e
            return is_correct
