"""Provides a client for making API requests."""

from typing import Type

import httpx

from wse.core.api.auth import AuthAPI
from wse.core.api.methods import HTTPMethod
from wse.core.auth.service import AuthService


class ApiClient:
    """Handles HTTP requests to the API."""

    def __init__(self, auth_service: AuthService, auth_api: AuthAPI) -> None:
        """Construct the client."""
        self._auth_service = auth_service
        self._auth_api = auth_api

    def request(
        self,
        method: str,
        endpoint: str,
        **kwargs: object,
    ) -> httpx.Response:
        """HTTP request."""
        return self._auth_api.perform_request(
            Type[HTTPMethod], endpoint, **kwargs
        )

    def get(self, endpoint: str, **kwargs: object) -> httpx.Response:
        """Send a GET request to the specified endpoint."""
        return self._auth_api.perform_request(
            HTTPMethod.GET, endpoint, **kwargs
        )

    def post(self, endpoint: str, **kwargs: object) -> httpx.Response:
        """Send a POST request to the specified endpoint."""
        return self._auth_api.perform_request(
            HTTPMethod.POST, endpoint, **kwargs
        )

    def put(self, endpoint: str, **kwargs: object) -> httpx.Response:
        """Send a PUT request to the specified endpoint."""
        return self._auth_api.perform_request(
            HTTPMethod.PUT, endpoint, **kwargs
        )

    def patch(self, endpoint: str, **kwargs: object) -> httpx.Response:
        """Send a PATCH request to the specified endpoint."""
        return self._auth_api.perform_request(
            HTTPMethod.PATCH, endpoint, **kwargs
        )

    def delete(self, endpoint: str, **kwargs: object) -> httpx.Response:
        """Send a DELETE request to the specified endpoint."""
        return self._auth_api.perform_request(
            HTTPMethod.DELETE, endpoint, **kwargs
        )
