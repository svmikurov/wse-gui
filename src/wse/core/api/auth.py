"""Handles API requests related to authentication."""

from typing import Dict, Optional
from urllib.parse import urljoin

import httpx

from wse.core.api.exceptions import AuthenticationError
from wse.core.api.methods import HTTPMethod
from wse.core.logger import setup_logger
from wse.interfaces.icore import IAuthAPI

logger = setup_logger('core.api.AuthAPI')


class AuthAPI(IAuthAPI):
    """Manages authentication-related API requests."""

    def __init__(
        self,
        base_url: str,
        request_timeout: int,
        endpoints: Dict[str, str],
    ) -> None:
        """Construct the authentication api handler."""
        self.base_url = base_url
        self.request_timeout = request_timeout
        self.endpoints = endpoints

    async def _request(
        self,
        method: str,
        endpoint: str,
        token: Optional[str] = None,
        **kwargs: Dict[str, str],
    ) -> httpx.Response:
        """Request by method."""
        url = urljoin(self.base_url, endpoint)

        headers = kwargs.get('headers', {})
        if token:
            headers['Authorization'] = f'Token {token}'

        try:
            async with httpx.AsyncClient(
                timeout=self.request_timeout
            ) as client:
                response = await client.request(
                    method,
                    url,
                    headers=headers,
                    **kwargs,
                )
            logger.info(
                f'Request to {endpoint} completed '
                f'with status {response.status_code}'
            )
            return response

        except httpx.HTTPStatusError as e:
            logger.error(f'HTTP error {response.status_code}: {e}')
            raise

        except httpx.RequestError as e:
            logger.error(f'Request error: {e}')
            raise

    async def authenticate(self, username: str, password: str) -> str:
        """Authenticate the user and retrieve an auth token."""
        try:
            response = await self._request(
                HTTPMethod.POST,
                self.endpoints['login'],
                json={'username': username, 'password': password},
            )
            return response.json()['auth_token']

        except httpx.HTTPError as e:
            logger.error(f'Authentication failed: {e}')
            raise AuthenticationError('Invalid credentials') from e

    async def validate_token(self, token: str) -> bool:
        """Validate the provided authentication token."""
        try:
            await self._request(
                HTTPMethod.GET,
                self.endpoints['validate_token'],
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
