"""Authentication service."""

from wse.core.config import Settings
from wse.core.storage.token_storage import TokenStorage
from wse.interfaces.iservices import IAuthService


class  AuthService(IAuthService):
    """Authentication service."""

    def __init__(self, settings: Settings) -> None:
        """Construct the service."""
        self.settings = settings
        self.token_storage: TokenStorage = self._get_token_storage(settings)

    def _get_token_storage(self, settings: Settings) -> TokenStorage:
        pass

    def is_authenticated(self) -> bool:
        """Is authenticated user."""
        return True
