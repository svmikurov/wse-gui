"""Handling API requests related to authentication."""

import logging
from typing import Dict, Optional
from urllib.parse import urljoin

import httpx

from wse.core.api.exceptions import AuthenticationError
from wse.core.api.http_methods import HTTPMethod
from wse.core.config import APIConfig
from wse.interfaces.icore import IAuthAPI

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


class AuthAPI(IAuthAPI):
    """Handles API requests related to authentication.

    :param config: Configuration for API endpoints.
    """

    def __init__(self, config: APIConfig) -> None:
        """Construct the authentication api handler."""
        self.config = config

    async def _request(
        self,
        method: str,
        endpoint: str,
        token: Optional[str] = None,
        **kwargs: Dict[str, str],
    ) -> httpx.Response:
        """Request by method."""
        headers = kwargs.get('headers', {})
        if token:
            headers['Authorization'] = f'Token {token}'

        try:
            async with httpx.AsyncClient(
                timeout=self.config.REQUEST_TIMEOUT
            ) as client:
                response = await client.request(
                    method,
                    urljoin(self.config.base_url, endpoint),
                    headers=headers,
                    **kwargs,
                )
            return response

        except httpx.HTTPStatusError as e:
            logger.error(f'HTTP error {response.status_code}: {e}')
            raise

        except httpx.RequestError as e:
            logger.error(f'Request error: {e}')
            raise

    async def authenticate(self, username: str, password: str) -> str:
        """Authenticate the user and retrieve the auth token."""
        try:
            response = await self._request(
                HTTPMethod.POST,
                self.config.LOGIN,
                json={'username': username, 'password': password},
            )
            return response.json()['token']

        except httpx.HTTPError as e:
            logger.error(f'Authentication failed: {e}')
            raise AuthenticationError('Invalid credentials') from e

    async def validate_token(self, token: str) -> bool:
        """Check is the current token is valid."""
        try:
            await self._request(
                HTTPMethod.GET,
                self.config.VALIDATE_TOKEN,
                token=token,
            )
            return True

        except httpx.HTTPError as e:
            logger.error(f'Token validation failed: {e}')
            return False

    async def perform_request(
        self,
        method: HTTPMethod,
        endpoint: str,
        token: Optional[str] = None,
        **kwargs: object,
    ) -> httpx.Response:
        """Public method for performing HTTP request."""
        return await self._request(method, endpoint, token=token, **kwargs)
