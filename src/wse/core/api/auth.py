"""Handles API requests related to authentication."""

import logging

import httpx

from wse.core.api.methods import HTTPMethod

logger = logging.getLogger(__name__)


class AuthAPI:
    """Manages authentication-related API requests."""

    def __init__(
        self,
        base_url: str,
        endpoints: dict[str, str],
    ) -> None:
        """Construct the service."""
        self.base_url = base_url
        self.endpoints = endpoints

    def _request(
        self,
        method: HTTPMethod,
        endpoints: str,
        token: str,
        **kwargs: object,
    ) -> httpx.Response:
        ...

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
