"""Manages user authentication and token validation."""

import logging

from wse.core.api.exceptions import AuthenticationError
from wse.interface.icore import IAuthAPI, ITokenStorage

logger = logging.getLogger(__name__)


class AuthService:
    """Handles authentication logic and token management."""

    def __init__(
        self,
        auth_api: IAuthAPI,
        token_storage: ITokenStorage,
    ) -> None:
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

        return self.is_authenticated()

    def is_authenticated(self) -> bool:
        """Check if the user is authenticated."""
        if self._auth_api.validate_token(self._token):
            logger.info('User is authenticated')
            return True
        else:
            logger.info('User is not authenticated')
            return False

    def close(self) -> None:
        """Close API client."""
        try:
            self._auth_api.close()
            logger.info('The authentication service has terminated.')
        except Exception as e:
            logger.exception(f'Error closing service: {e}')
