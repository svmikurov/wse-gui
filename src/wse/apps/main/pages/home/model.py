"""Defines Home page model."""

from dataclasses import dataclass
from typing import Literal

from injector import inject
from typing_extensions import override

from wse.core.auth import AuthServiceProto
from wse.feature.base.mixins import AddObserverGeneric

from .abc import HomeModelFeature

_NotifyType = Literal[
    'user_authenticated',
    'user_anonymous',
]


class _Feature(
    HomeModelFeature,
    AddObserverGeneric[_NotifyType],
):
    """Home page model feature."""

    _auth_service: AuthServiceProto

    @override
    def check_auth_status(self) -> None:
        """Check user authentication status."""
        if self._auth_service.is_auth:
            self._notify('user_authenticated')
        else:
            self._notify('user_anonymous')

    @override
    def logout(self) -> None:
        """Handle the logout event."""
        self._auth_service.logout()
        self.check_auth_status()


@inject
@dataclass
class HomeModel(
    _Feature,
    AddObserverGeneric[_NotifyType],
):
    """Home page model."""

    _auth_service: AuthServiceProto
