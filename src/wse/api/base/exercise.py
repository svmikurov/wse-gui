"""Base api client."""

import logging
from abc import ABC, abstractmethod
from typing import Type, TypeVar

import httpx
from injector import inject
from pydantic import ValidationError

from wse.core.http import AuthSchemaABC, HttpClientABC
from wse.feature.services import Answer

from .. import responses
from ..main.abc import ExerciseApiABC, ExerciseT_contra

log = logging.getLogger(__name__)

# TODO: Fix TypeVar definition
T = TypeVar('T', responses.QuestionResponse, responses.ResultResponse)


class BaseExerciseApi(
    ExerciseApiABC[ExerciseT_contra],
    ABC,
):
    """Base exercise api client."""

    @inject
    def __init__(
        self,
        http_client: HttpClientABC,
        auth_scheme: AuthSchemaABC,
    ) -> None:
        """Construct the client."""
        self._http_client = http_client
        self._auth_scheme = auth_scheme

    @abstractmethod
    def request_task(
        self,
        exercise: ExerciseT_contra,
    ) -> responses.QuestionResponse | None:
        """Request a task from the server."""

    @abstractmethod
    def check_answer(
        self,
        answer: Answer,
        exercise: ExerciseT_contra,
    ) -> responses.ResultResponse | None:
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
            log.exception(
                f'Validation error parsing API response: {response.json()}'
            )
            return None

        except (ValueError, TypeError):
            log.exception('Parsing JSON error')
            return None
