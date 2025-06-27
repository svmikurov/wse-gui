"""Defines Authentication page controller."""

from dataclasses import dataclass

from injector import inject

from wse.config.settings import SUCCESS_REDIRECT
from wse.features.base.mvc import BasePageController
from wse.features.subapps.main.pages.auth.interfaces import IAuthView


@inject
@dataclass
class AuthController(BasePageController):
    """Authentication page controller."""

    _view: IAuthView

    # Notifications
    def success_authentication(self) -> None:
        """Notify about successful authentication."""
        self.navigate(SUCCESS_REDIRECT)
