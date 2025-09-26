"""Account UI state."""

import logging
from dataclasses import dataclass, replace
from typing import TypedDict

import toga
from injector import inject
from typing_extensions import Unpack

from wse.core.auth import AuthServiceProto
from wse.core.interfaces import Navigable
from wse.ui.base.mixins import SetAuthStatusMixin
from wse.ui.base.navigate.mixin import NavigateStateMixin
from wse.ui.main.account.abc import AuthViewModelABC

audit = logging.getLogger(__name__)


class _DataFieldType(TypedDict, total=False):
    """Fields for Authenticate UI state data."""

    username: str
    password: str
    is_auth: bool


@dataclass(frozen=True)
class AuthUIState:
    """Authenticate UI state data."""

    username: str | None = None
    password: str | None = None
    is_auth: bool = False


@inject
@dataclass
class AuthViewModel(
    SetAuthStatusMixin,
    NavigateStateMixin,
    AuthViewModelABC,
):
    """Account UI state the ViewModel."""

    _navigator: Navigable
    _auth_service: AuthServiceProto

    def __post_init__(self) -> None:
        """Construct the state."""
        self._create_data()

    # API

    def refresh_context(self) -> None:
        """Refresh screen context."""
        self._set_auth_state()

    def handle_success_authentication(self) -> None:
        """Handle the success authentication."""
        self._set_auth_state()

    # Callback methods

    def logout(self, _: toga.Button) -> None:
        """Logout, button callback method."""
        self._auth_service.logout()
        self._set_auth_state()

    # Utility methods

    def _create_data(self) -> None:
        """Create UI state data."""
        self._data = AuthUIState()

    def _update_data(self, **data: Unpack[_DataFieldType]) -> None:
        """Update UI state data."""
        replace(self._data, **data)

    # On screen close event

    def on_close(self) -> None:
        """Call methods before close the screen."""
        audit.debug(f'Have no `on_close()`: {self.__class__.__name__}')
