"""Defines protocol for API client interface."""

from typing import Any, Protocol

from httpx import Response


class IApiClient(
    Protocol,
):
    """Protocol for API client interface."""

    def get(self, endpoint: str) -> Response:
        """Request with GET method."""

    def post(self, endpoint: str, data: dict[str, Any]) -> Response:
        """Request with POST method."""
