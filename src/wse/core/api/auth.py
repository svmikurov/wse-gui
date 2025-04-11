"""Handles API requests related to authentication."""

import logging
from urllib.parse import urljoin

import httpx

from wse.core.api.methods import HTTPMethod

logger = logging.getLogger(__name__)


class AuthAPI:
    """Manages authentication-related API requests."""

    def __init__(
        self,
        base_url: str,
        client: httpx.Client,
        endpoints: dict[str, str],
    ) -> None:
        """Construct the service."""
        self.base_url = base_url
        self.endpoints = endpoints
        self.client = client

    def _request(
        self,
        method: HTTPMethod,
        endpoint: str,
        token: str,
        **kwargs: dict[str, str],
    ) -> httpx.Response:
        """Request by method."""
        url = urljoin(self.base_url, endpoint)

        # Add token to request headers
        headers = kwargs.get('headers', {})
        if token:
            headers['Authorization'] = f'Token {token}'

        try:
            response = self.client.request(
                method,
                url,
                headers=headers,
                **kwargs,
            )
            logger.debug(
                f'Request to {endpoint} completed '
                f'with status {response.status_code}'
            )
            return response

        except httpx.HTTPStatusError as e:
            logger.exception(f'HTTP error {e.response.status_code}: {e}')
            raise

        except httpx.HTTPError as e:
            logger.exception(f'Request error: {e}')
            raise

    def validate_token(self, token: str) -> bool:
        """Validate the provided authentication token."""
        try:
            self._request(
                HTTPMethod.GET,
                self.endpoints['validate_token'],
                token=token,
            )
            return True

        except httpx.HTTPError as e:
            logger.exception(f'Token validation failed: {e}')
            return False
