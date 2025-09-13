"""Account UI state."""

from dataclasses import dataclass, replace
from typing import TypedDict

import toga
from injector import inject
from typing_extensions import Unpack

from wse.apps.nav_id import NavID
from wse.core.auth import AuthServiceProto
from wse.core.interfaces import Navigable
from wse.ui.main.account.abc import AuthViewModelABC


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
class AuthViewModel(AuthViewModelABC):
    """Account UI state the ViewModel."""

    _navigator: Navigable
    _auth_service: AuthServiceProto

    def __post_init__(self) -> None:
        """Construct the state."""
        self._create_data()

    # API

    # TODO: Move to base class.
    def refresh_context(self) -> None:
        """Refresh screen context."""
        self._set_auth_state()

    # TODO: Move to base class.
    def navigate(self, nav_id: NavID) -> None:
        """Handle the navigate event, callback."""
        self._navigator.navigate(nav_id=nav_id)

    # Callback methods

    def logout(self, _: toga.Button) -> None:
        """Logout, button callback method."""
        self._auth_service.logout()
        self._set_auth_state()

    # Feature

    def handle_success_authentication(self) -> None:
        """Handle the success authentication."""
        self._set_auth_state()

    # Utility methods

    # TODO: Move to ABC Generic[...UIState] class.
    def _create_data(self) -> None:
        """Create UI state data."""
        self._data = AuthUIState()

    # TODO: Move to ABC Generic[...UIState] class.
    def _update_data(self, **data: Unpack[_DataFieldType]) -> None:
        """Update UI state data."""
        replace(self._data, **data)

    # TODO: Move to mixin.
    def _set_auth_state(self) -> None:
        """Set user authenticated state."""
        if is_auth := self._auth_service.is_auth:
            self._notify('user_authenticated')
        else:
            self._notify('user_anonymous')

        self._update_data(is_auth=is_auth)
