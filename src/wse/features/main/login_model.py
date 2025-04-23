"""Defines login page model."""

import logging

from wse.core.navigation.navigation_id import NavigationID
from wse.features.base.mvc import BaseModel
from wse.interface.icore import IAuthService

logger = logging.getLogger(__name__)


class LoginModel(BaseModel):
    """Login page model."""

    def __init__(
        self,
        *args: object,
        auth_service: IAuthService,
        **kwargs: object,
    ) -> None:
        """Construct the model."""
        super().__init__(*args, **kwargs)
        self._auth_service = auth_service

    def login(self, username: str, password: str) -> None:
        """Authenticate the user."""
        result = self._auth_service.authenticate(username, password)

        if result:
            self._subject.notify('navigate', nav_id=NavigationID.ACCOUNT)

    def _set_context(self) -> None:
        """Set view context for render into view."""
        ...

    def _notify_render_context(self) -> None:
        """Notify controller to fill view with context."""
        ...
