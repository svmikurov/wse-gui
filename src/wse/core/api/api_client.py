"""API client."""

import logging

import httpx

from wse.core.api.auth_api import AuthAPI
from wse.core.api.http_methods import HTTPMethod
from wse.core.auth.auth import AuthService
from wse.interfaces.icore import IApiClient

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s -%(message)s',
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


class ApiClient(IApiClient):
    """Client for working with API."""

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
        """Request get method."""
        return await self._auth_api.perform_request(
            HTTPMethod.GET, endpoint, **kwargs
        )

    async def post(self, endpoint: str, **kwargs: object) -> httpx.Response:
        """Request post method."""
        return await self._auth_api.perform_request(
            HTTPMethod.POST, endpoint, **kwargs
        )

    async def put(self, endpoint: str, **kwargs: object) -> httpx.Response:
        """Request put method."""
        return await self._auth_api.perform_request(
            HTTPMethod.PUT, endpoint, **kwargs
        )

    async def patch(self, endpoint: str, **kwargs: object) -> httpx.Response:
        """Request patch method."""
        return await self._auth_api.perform_request(
            HTTPMethod.PATCH, endpoint, **kwargs
        )

    async def delete(self, endpoint: str, **kwargs: object) -> httpx.Response:
        """Request delete method."""
        return await self._auth_api.perform_request(
            HTTPMethod.DELETE, endpoint, **kwargs
        )
