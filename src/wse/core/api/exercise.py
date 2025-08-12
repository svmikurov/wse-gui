"""Defines exercise API."""

import logging
from typing import Any, cast

import httpx
from httpx import Response
from injector import inject
from typing_extensions import override

from wse.core.exceptions import ExerciseError
from wse.core.interfaces.iapi import IAuthScheme, IExerciseApiClient

from ...apps.math.http.config import MathAPIConfigV1
from ...apps.math.pages.simple_calc.dto import CalcAnswerDTO, CalcResultDTO
from ...core.http import IHttpClient

logger = logging.getLogger(__name__)


@inject
class ExerciseApiClient(IExerciseApiClient):
    """Exercise API client."""

    def __init__(
        self,
        auth_scheme: IAuthScheme,
        http_client: IHttpClient,
        api_config: MathAPIConfigV1,
    ) -> None:
        """Construct the API."""
        self._auth_scheme = auth_scheme
        self._http_client = http_client
        # Endpoints
        self._get_task_endpoint = api_config.calculation['get_task']
        self._validate_endpoint = api_config.calculation['validate_answer']

    @override
    def request_task(self, data: dict[str, Any]) -> dict[str, Any]:
        """Request the task."""
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
    def check_answer(self, answer: CalcAnswerDTO) -> CalcResultDTO:
        """Check the user entered answer."""
        try:
            response: Response = self._http_client.post(
                url=self._validate_endpoint,
                json=answer.to_dict(),
                auth=cast(httpx.Auth, self._auth_scheme),
            )

        except httpx.HTTPStatusError:
            logger.error('Http client error')
            raise

        else:
            try:
                result_dto = CalcResultDTO.from_dict(response.json())
            except AttributeError as e:
                raise ExerciseError from e
            return result_dto
