"""Defines login page model."""

import logging

from wse.core.auth.service import AuthService
from wse.core.navigation.navigation_id import NavigationID
from wse.features.base.mvc import BaseModel

logger = logging.getLogger(__name__)


class LoginModel(BaseModel):
    """Login page model."""

    def __init__(
        self,
        *args: object,
        auth_service: AuthService,
        **kwargs: object,
    ) -> None:
        """Construct the model."""
        super().__init__(*args, **kwargs)
        self._auth_service = auth_service

    def login(self, username: str, password: str) -> None:
        """Authenticate the user."""
        if self._auth_service.authenticate(username, password):
            self._handel_success_login()

    def is_authenticated(self) -> bool:
        """Check user is authenticated."""
        return self._auth_service.is_authenticated()

    # Notification
    def _handel_success_login(self) -> None:
        self._subject.notify('navigate', nav_id=NavigationID.ACCOUNT)
        self._subject.notify('clear_input_fields')
