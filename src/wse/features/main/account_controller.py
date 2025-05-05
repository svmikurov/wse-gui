"""Defines Account page controller."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from http import HTTPStatus
from typing import TYPE_CHECKING

from wse.core.navigation.navigation_id import NavID
from wse.features.base.mvc import ContextController

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from wse.features.main import AccountModel, AccountView


@dataclass(kw_only=True)
class AccountController(ContextController):
    """Account page controller."""

    _CHECK_TOKEN_PATH = '/api/v1/auth/users/me/'

    model: AccountModel
    view: AccountView

    def request_context(self) -> None:
        """Request context from the model."""
        self.model.render_context()

    def render_auth_context(self) -> None:
        """Render the auth context into view."""
        self.view.update_auth_button(NavID.LOGIN)

    def render_not_auth_context(self) -> None:
        """Render context for non-authenticated user."""
        self.view.update_auth_button(NavID.LOGOUT)

    def logout(self) -> None:
        """Logout from account."""
        self.model.logout()

    # Listener methods
    def handel_success_logout(self) -> None:
        """Update account widgets on success logout."""
        self.render_auth_context()

    # Notifications
    def navigate(self, nav_id: NavID) -> None:
        """Navigate to page, the button event listener."""
        # Logout button now has no navigation.
        if nav_id == NavID.LOGOUT:
            return self.logout()

        self._subject.notify('navigate', nav_id=nav_id)

    ####################################################################
    # View listener methods

    def check_token(self) -> None:
        """Check auth token."""
        response = self.model.api_client.get(self._CHECK_TOKEN_PATH)
        answer = 'authentication token is not valid'
        if response.status_code == HTTPStatus.OK:
            answer = 'authentication token is valid'
        self.view.info_panel.change(answer)

    def clean_panel(self) -> None:
        """Clean text panel."""
        self.view.info_panel.clean()
