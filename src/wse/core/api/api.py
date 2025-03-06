"""Provides a client for making API requests."""

import httpx

from wse.core.api.auth import AuthAPI
from wse.core.api.methods import HTTPMethod
from wse.core.auth.auth import AuthService
from wse.interfaces.icore import IApiClient


class ApiClient(IApiClient):
    """Handles HTTP requests to the API."""

    def __init__(self, auth_service: AuthService) -> None:
        """Construct the client."""
        self._auth_service = auth_service
        self._auth_api = AuthAPI(auth_service.settings.api)

    async def _request(
        self,
        method: str,
        endpoint: str,
        **kwargs: object,
    ) -> httpx.Response:
        return await self._auth_api.perform_request(method, endpoint, **kwargs)

    async def get(self, endpoint: str, **kwargs: object) -> httpx.Response:
        """Send a GET request to the specified endpoint."""
        return await self._auth_api.perform_request(
            HTTPMethod.GET, endpoint, **kwargs
        )

    async def post(self, endpoint: str, **kwargs: object) -> httpx.Response:
        """Send a POST request to the specified endpoint."""
        return await self._auth_api.perform_request(
            HTTPMethod.POST, endpoint, **kwargs
        )

    async def put(self, endpoint: str, **kwargs: object) -> httpx.Response:
        """Send a PUT request to the specified endpoint."""
        return await self._auth_api.perform_request(
            HTTPMethod.PUT, endpoint, **kwargs
        )

    async def patch(self, endpoint: str, **kwargs: object) -> httpx.Response:
        """Send a PATCH request to the specified endpoint."""
        return await self._auth_api.perform_request(
            HTTPMethod.PATCH, endpoint, **kwargs
        )

    async def delete(self, endpoint: str, **kwargs: object) -> httpx.Response:
        """Send a DELETE request to the specified endpoint."""
        return await self._auth_api.perform_request(
            HTTPMethod.DELETE, endpoint, **kwargs
        )
