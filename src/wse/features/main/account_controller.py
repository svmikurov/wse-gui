"""Defines account page controller."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from wse.core.navigation.navigation_id import NavigationID
from wse.features.base.mvc import ContextController

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from wse.features.main import AccountModel, AccountView


@dataclass(kw_only=True)
class AccountController(ContextController):
    """Account page controller."""

    model: AccountModel
    view: AccountView

    def request_context(self) -> None:
        """Request context from the model."""
        self.model.render_context()

    def render_auth_context(self) -> None:
        """Render the auth context into view."""
        logger.debug('Render the context for auth')
        self.view.update_auth_button(NavigationID.LOGIN)

    def render_not_auth_context(self) -> None:
        """Render context for non-authenticated user."""
        logger.debug('Render the context for nor auth')
        self.view.update_auth_button(NavigationID.LOGOUT)
