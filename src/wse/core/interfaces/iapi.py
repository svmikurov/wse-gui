"""Defines protocol for API client interface."""

from typing import Any, Protocol

from httpx import Response
from wse_exercises.core.mathem.enums import Exercises


class IApiClient(
    Protocol,
):
    """Protocol for API client interface."""

    def get(self, endpoint: str) -> Response:
        """Request with GET method."""

    def post(self, endpoint: str, data: dict[str, Any]) -> Response:
        """Request with POST method."""


class IExerciseApi(
    Protocol,
):
    """Defines protocol for exercise API."""

    def request_task(self, exercise: Exercises) -> dict[str, Any]:
        """Request the task."""
