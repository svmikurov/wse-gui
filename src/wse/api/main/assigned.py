"""The api client for assigned exercise in text repr of components.

Defines api client for http request of assigned exercise with string
representation of task components.
"""

import logging
from typing import Any, TypeVar

import httpx
from typing_extensions import override

from .. import responses
from ..base.exercise import BaseExerciseApi
from ..schemas.exercise import Assigned
from ..schemas.task import Answer

log = logging.getLogger(__name__)

T = TypeVar('T', responses.QuestionResponse, responses.ResultResponse)


class AssignedApiClient(BaseExerciseApi[Any]):
    """Assigned exercise api client with text task."""

    @override
    def request_task(
        self,
        exercise: Assigned,
    ) -> responses.QuestionResponse | None:
        """Request assigned exercise task."""
        try:
            response: httpx.Response = self._http_client.get(
                url=exercise.question_url_path,
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
        answer: Answer,
        exercise: Assigned,
    ) -> responses.ResultResponse | None:
        """Check user answer on assigned exercise task."""
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
