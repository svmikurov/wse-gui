"""Defines the data model for the authentication feature."""
import logging

from wse.core.auth.service import AuthService
from wse.core.navigation.routes import Routes
from wse.features.auth.login_validator import (
    validate_password,
    validate_username,
)
from wse.features.shared.observer import Subject

logger = logging.getLogger(__name__)


class UserModel:
    """User model."""

    def __init__(self, auth_service: AuthService) -> None:
        """Construct the model."""
        super().__init__()
        self.auth_service = auth_service
        self.subject = Subject()
        self.username: str | None = None
        self.password: str | None = None

    async def authenticate(self, username: str, password: str) -> None:
        """Authenticate user."""
        if await self._validate_credentials(username, password):
            await self.auth_service.authenticate(username, password)

            if await self.auth_service.is_authenticated():
                self.subject.notify('navigate', route=Routes.HOME)
            else:
                # TODO: Add authentication error display.
                self.subject.notify(
                    'show_credentials_error',
                    error='Credentials error',
                )

    async def _validate_credentials(
        self,
        username: str,
        password: str,
    ) -> bool:
        username_errors = validate_username(username)
        password_errors = validate_password(password)

        if not username_errors and not password_errors:
            return True

        if username_errors:
            self.subject.notify('show_username_errors', errors=username_errors)
        if password_errors:
            self.subject.notify('show_password_errors', errors=password_errors)
            return False
