"""Defines the data model for the authentication feature."""

from wse.core.auth.service import AuthService
from wse.core.logger import setup_logger
from wse.core.navigation.routes import Routes
from wse.features.shared.observer import Subject

logger = setup_logger('features.auth.UserModel')


class UserModel(Subject):
    """User model."""

    def __init__(self, auth_service: AuthService) -> None:
        """Construct the model."""
        super().__init__()
        self.auth_service = auth_service
        self.username: str | None = None
        self.password: str | None = None

    async def authenticate(self, username: str, password: str) -> None:
        """Authenticate user."""
        await self.auth_service.authenticate(username, password)

        if await self.auth_service.is_authenticated():
            self.notify('navigate', route=Routes.HOME)
