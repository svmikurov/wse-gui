"""The api client for assigned exercise in text repr of components.

Defines api client for http request of assigned exercise with string
representation of task components.
"""

import logging
from typing import TypeVar

import httpx
from typing_extensions import override

from wse.core.api import QuestionResponse, ResultResponse
from wse.feature.api.main.abc import AssignedApiClientABC
from wse.feature.services import Answer
from wse.feature.shared.schemas.exercise import Assigned

logger = logging.getLogger(__name__)

T = TypeVar('T', QuestionResponse, ResultResponse)


class AssignedApiClient(AssignedApiClientABC):
    """Assigned exercise api client with text task."""

    @override
    def request_task(
        self,
        exercise: Assigned,
    ) -> QuestionResponse | None:
        """Request assigned exercise task."""
        try:
            response: httpx.Response = self._http_client.get(
                url=exercise.question_url_path,
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
        exercise: Assigned,
    ) -> ResultResponse | None:
        """Check user answer on assigned exercise task."""
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
