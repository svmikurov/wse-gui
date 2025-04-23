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

        return self.check_auth()


    def check_auth(self) -> bool:
        """Check if the user is authenticated."""
        if not self._token:
            logger.debug('User is not authenticated')
            return False
        return self._auth_api.validate_token(self._token)

    def set_auth_status(self) -> None:
        """Set user authentication status."""
        logger.debug('Called `set_auth_status` method')
