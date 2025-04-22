"""Defines account page controller."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from wse.core.navigation.navigation_id import NavigationID
from wse.features.base.mvc import ContextController
from wse.interface.ifeatures import IContext

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from wse.features.main import AccountView


@dataclass
class AccountController(ContextController):
    """Account page controller."""

    view: AccountView

    def render_context(self, context: IContext) -> None:
        """Render the context into view."""

    def render_auth_context(self) -> None:
        """Render the auth context into view."""
        self.view.update_auth_button(NavigationID.LOGOUT)

    def render_not_auth_context(self) -> None:
        """Render context for non-authenticated user."""
        self.view.update_auth_button(NavigationID.LOGIN)
