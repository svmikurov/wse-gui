"""Manages user authentication and token validation."""

from typing import Dict, Optional

from wse.config.config import Settings
from wse.core.api.auth import AuthAPI
from wse.core.api.exceptions import AuthenticationError
from wse.core.logger import setup_logger
from wse.core.storage.token import TokenStorage
from wse.interfaces.icore import IAuthService

logger = setup_logger('auth.AuthService')


class AuthService(IAuthService):
    """Handles authentication logic and token management."""

    def __init__(self, settings: Settings, endpoints: Dict[str, str]) -> None:
        """Construct the service."""
        self.token_storage: TokenStorage = self._get_token_storage(settings)
        self._auth_api = AuthAPI(
            settings.base_url, settings.REQUEST_TIMEOUT, endpoints
        )
        # Auth token loads from storage, is None by default.
        self._token: Optional[str] = None
        self._load_token()

    def _load_token(self) -> None:
        self._token = self.token_storage.load_token()

    @staticmethod
    def _get_token_storage(settings: Settings) -> TokenStorage:
        return TokenStorage(
            settings.storage_config.token_file,
            settings.storage_config.encryption_key.get_secret_value(),
        )

    async def is_authenticated(self) -> bool:
        """Check if the user is authenticated."""
        if not self._token:
            return False
        return await self._auth_api.validate_token(self._token)

    async def authenticate(self, username: str, password: str) -> None:
        """Authenticate the user with the provided credentials."""
        try:
            self._token = await self._auth_api.authenticate(username, password)
            self.token_storage.save_token(self._token)
            logger.info('Authentication successful')
        except AuthenticationError as e:
            logger.error(f'Authentication failed for user {username}: {e}')
            raise

    async def close(self) -> None:
        """Close API client."""
        try:
            await self._auth_api.close()
            logger.info('The authentication service has terminated.')
        except Exception as e:
            logger.error(f'Error closing service: {e}', exc_info=True)
