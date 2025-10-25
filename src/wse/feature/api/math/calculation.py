"""Defines exercise API."""

import logging

import httpx
from injector import inject
from typing_extensions import override

from wse.core.api.base import ExerciseApi
from wse.core.api.response import QuestionResponse, ResultResponse
from wse.feature.api.math import Calculation
from wse.feature.services import Answer

from .protocol import CalculationApiProto

logger = logging.getLogger(__name__)


@inject
class CalculationApiClient(
    ExerciseApi[Calculation],
    CalculationApiProto,
):
    """Exercise API client."""

    @override
    def request_task(
        self,
        exercise: Calculation,
    ) -> QuestionResponse | None:
        """Request the task."""
        try:
            response: httpx.Response = self._http_client.post(
                url=exercise.question_url_path,
                json=exercise.condition.to_dict(),
                auth=self._auth_scheme,
            )
            response.raise_for_status()

        except httpx.HTTPError:
            logger.exception('Request task error')
            return None

        return self._parse_response(response, QuestionResponse)

    @override
    def check_answer(
        self,
        answer: Answer,
        exercise: Calculation,
    ) -> ResultResponse | None:
        """Check the user entered answer."""
        try:
            response: httpx.Response = self._http_client.post(
                url=exercise.check_url_path,
                json=answer.to_dict(),
                auth=self._auth_scheme,
            )
            response.raise_for_status()

        except httpx.HTTPError:
            logger.exception('Check answer error')
            return None

        return self._parse_response(response, ResultResponse)
