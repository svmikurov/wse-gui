"""Defines exercise API."""

import logging

import httpx
from injector import inject
from typing_extensions import override

from wse.feature import services

from .. import responses
from ..main.exercise import ExerciseApi
from . import CalculationApiABC, schemas

log = logging.getLogger(__name__)


@inject
class CalculationApiClient(
    ExerciseApi[schemas.Calculation],
    CalculationApiABC,
):
    """Exercise API client."""

    @override
    def request_task(
        self,
        exercise: schemas.Calculation,
    ) -> responses.QuestionResponse | None:
        """Request the task."""
        try:
            response: httpx.Response = self._http_client.post(
                url=exercise.question_url_path,
                json=exercise.condition.to_dict(),
                auth=self._auth_scheme,
            )
            response.raise_for_status()

        except httpx.HTTPError:
            log.exception('Request task error')
            return None

        return self._parse_response(response, responses.QuestionResponse)

    @override
    def check_answer(
        self,
        answer: services.Answer,
        exercise: schemas.Calculation,
    ) -> responses.ResultResponse | None:
        """Check the user entered answer."""
        try:
            response: httpx.Response = self._http_client.post(
                url=exercise.check_url_path,
                json=answer.to_dict(),
                auth=self._auth_scheme,
            )
            response.raise_for_status()

        except httpx.HTTPError:
            log.exception('Check answer error')
            return None

        return self._parse_response(response, responses.ResultResponse)
