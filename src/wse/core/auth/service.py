"""Manages user authentication and token validation."""

import logging

import httpx

from wse.core.api.auth import AuthAPI
from wse.core.api.exceptions import AuthenticationError
from wse.core.storage.token import TokenStorage

logger = logging.getLogger(__name__)


class AuthService:
    """Handles authentication logic and token management."""

    def __init__(self, auth_api: AuthAPI, token_storage: TokenStorage) -> None:
        """Construct the service."""
        self._auth_api = auth_api
        self._token_storage = token_storage
        self._token: str | None = None

    def authenticate(self, username: str, password: str) -> bool | None:
        """Authenticate the user."""
        try:
            self._token = self._auth_api.authenticate(username, password)

        except AuthenticationError as e:
            logger.exception(f'Authentication failed for user {username}: {e}')
            raise

        if self._token:
            self._token_storage.save_token(self._token)
            logger.info('Authentication successful')

        # Checking the received token
        return self.is_authenticated()

    def is_authenticated(self) -> bool:
        """Check if the user is authenticated."""
        self._retrieve_token()
        if not self._token:
            return False

        if self._auth_api.validate_token(self._token):
            logger.info('User is authenticated')
            return True
        else:
            logger.info('User is not authenticated')
            return False

    def _retrieve_token(self) -> None:
        self._token = self._token_storage.load_token()

    def get_token(self) -> str:
        """Get auth token."""
        return self._token

    def close(self) -> None:
        """Close API client."""
        try:
            self._auth_api.close()
            logger.info('The authentication service has terminated.')
        except Exception as e:
            logger.exception(f'Error closing service: {e}')

    def logout(self) -> bool:
        """Logout from account."""
        try:
            self._auth_api.logout(self._token)
        except httpx.HTTPError as e:
            logger.warning(f'Logout failed: {e}')
            return False
        else:
            self._token_storage.delete_token()
            logger.info('Success logout')
            return True
