"""Defines Authentication page model."""

from injector import inject
from typing_extensions import override

from wse.core.interfaces.iauth import IAuthService
from wse.features.base import BaseModel
from wse.features.subapps.nav_id import NavID

from .interfaces import IAuthModel


@inject
class AuthModel(
    BaseModel,
    IAuthModel,
):
    """Authentication page model."""

    _auth_service: IAuthService

    @override
    def handle_success_authentication(self) -> None:
        """Handle the success authentication."""
        self._notify('credential_clean')
        self._notify('navigate', nav_id=NavID.HOME)
