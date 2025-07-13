"""Defines Home page model."""

from dataclasses import dataclass

from injector import inject
from typing_extensions import override

from wse.core.interfaces.iauth import IAuthService
from wse.features.base import BaseModel
from wse.features.subapps.main.pages.home.interfaces import IHomeModel


@inject
@dataclass
class HomeModel(
    BaseModel,
    IHomeModel,
):
    """Home page model."""

    _auth_service: IAuthService

    @override
    def on_open(self) -> None:
        """Call model methods when page opens."""
        self._define_view_content()

    def _define_view_content(self) -> None:
        """Define view content by user auth state."""
        notification = 'user_authenticated'
        if not self._auth_service.is_auth:
            notification = 'user_anonymous'
        self._notify(notification)

    @override
    def handle_logout(self) -> None:
        """Handle the logout event."""
        self._auth_service.logout()
        self._define_view_content()
