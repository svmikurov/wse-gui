"""Base api client."""

import logging
from abc import ABC, abstractmethod
from typing import Generic, Type, TypeVar

import httpx
from injector import inject
from pydantic import ValidationError

from wse.feature.services import Answer

from ..http import AuthSchemaProto, HttpClientProto
from .protocol import ExerciseT_contra
from .response import QuestionResponse, ResultResponse

logger = logging.getLogger(__name__)

# TODO: Fix TypeVar definition
T = TypeVar('T', QuestionResponse, ResultResponse)


class ExerciseApi(
    ABC,
    Generic[ExerciseT_contra],
):
    """Base exercise api client."""

    @inject
    def __init__(
        self,
        http_client: HttpClientProto,
        auth_scheme: AuthSchemaProto,
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
            r_schema = response_schema(**response.json())
            return r_schema

        except ValidationError:
            logger.exception(
                f'Validation error parsing API response: {response.json()}'
            )
            return None

        except (ValueError, TypeError):
            logger.exception('Parsing JSON error')
            return None
