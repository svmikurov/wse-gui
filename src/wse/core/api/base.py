"""Base api client."""

import logging
from abc import ABC, abstractmethod
from typing import Type, TypeVar

import httpx
from injector import inject
from pydantic import ValidationError

from wse.feature.services import Answer

from ..http import AuthSchemeProto, HttpClientProto
from . import (
    QuestionResponse,
    ResultResponse,
)
from .protocol import (
    ExerciseApiProto,
    ExerciseT_contra,
)

logger = logging.getLogger(__name__)

# TODO: Fix TypeVar definition
T = TypeVar('T', QuestionResponse, ResultResponse)


class ExerciseApi(
    ABC,
    ExerciseApiProto[ExerciseT_contra],
):
    """Base exercise api client."""

    @inject
    def __init__(
        self,
        http_client: HttpClientProto,
        auth_scheme: AuthSchemeProto,
    ) -> None:
        """Construct the client."""
        self._http_client = http_client
        self._auth_scheme = auth_scheme

    @abstractmethod
    def request_task(
        self,
        exercise: ExerciseT_contra,
    ) -> QuestionResponse | None:
        """Request a task from the server."""

    @abstractmethod
    def check_answer(
        self,
        answer: Answer,
        exercise: ExerciseT_contra,
    ) -> ResultResponse | None:
        """Check on the server the user's entered answer."""

    @staticmethod
    def _parse_response(
        response: httpx.Response,
        response_schema: Type[T],
    ) -> T | None:
        try:
            return response_schema(**response.json())

        except ValidationError:
            logger.exception(
                f'Validation error parsing API response: {response.json()}'
            )
            return None

        except (ValueError, TypeError):
            logger.exception('Parsing JSON error')
            return None
