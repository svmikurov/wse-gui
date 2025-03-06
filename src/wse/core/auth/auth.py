"""Manages user authentication and token validation."""

from typing import Optional

from wse.core.api.auth_api import AuthAPI
from wse.core.config import Settings
from wse.core.logger import root_logger as logger
from wse.core.storage.token_storage import TokenStorage
from wse.interfaces.icore import IAuthService


class AuthService(IAuthService):
    """Handles authentication logic and token management."""

    def __init__(self, settings: Settings) -> None:
        """Construct the service."""
        self.settings = settings
        self.token_storage: TokenStorage = self._get_token_storage(settings)
        self._auth_api = AuthAPI(settings.api_config)
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
        self._token = await self._auth_api.authenticate(username, password)
        self.token_storage.save_token(self._token)
        logger.info('Authentication successful')
