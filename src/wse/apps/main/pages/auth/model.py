"""Defines Authentication page model."""

from dataclasses import dataclass
from typing import Literal

from injector import inject
from typing_extensions import override

from wse.apps.nav_id import NavID
from wse.core.auth import AuthServiceProto
from wse.feature.base.mixins import AddObserverGen

from .abc import AuthModelFeature

_NotifyType = Literal[
    'credential_clean',
    'navigate',
]


class _Feature(
    AddObserverGen[_NotifyType],
    AuthModelFeature,
):
    """Authentication page model feature."""

    @override
    def handle_success_authentication(self) -> None:
        """Handle the success authentication."""
        self._notify('credential_clean')
        self._notify('navigate', nav_id=NavID.HOME)


@inject
@dataclass
class AuthModel(
    _Feature,
):
    """Authentication page model."""

    _auth_service: AuthServiceProto
