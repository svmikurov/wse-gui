"""Defines Authentication page model."""

from dataclasses import dataclass

from injector import inject
from typing_extensions import override

from wse.apps.nav_id import NavID
from wse.core.interfaces.iauth import IAuthService
from wse.features.base import BaseModel

from ._abc import AuthModelABC


@inject
@dataclass
class AuthModel(
    BaseModel,
    AuthModelABC,
):
    """Authentication page model."""

    _auth_service: IAuthService

    @override
    def handle_success_authentication(self) -> None:
        """Handle the success authentication."""
        self._notify('credential_clean')
        self._notify('navigate', nav_id=NavID.HOME)
