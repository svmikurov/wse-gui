"""Mixins for UI layer."""

from typing import Callable

from wse.core.auth import AuthServiceProto
from wse.core.interfaces import Navigable
from wse.core.navigation.nav_id import NavID


class SetAuthStatusMixin:
    """Mixin providing set user auth status."""

    _auth_service: AuthServiceProto

    _notify: Callable[..., None]
    _update_data: Callable[..., None]

    def _set_auth_state(self) -> None:
        """Set user authenticated state."""
        if is_auth := self._auth_service.is_auth:
            self._notify('user_authenticated')
        else:
            self._notify('user_anonymous')

        self._update_data(is_auth=is_auth)


class NavigateMixin:
    """Mixin providing API for navigate event handle."""

    _navigator: Navigable

    def navigate(self, nav_id: NavID) -> None:
        """Handle the navigate event."""
        self._navigator.navigate(nav_id=nav_id)


class BalanceUpdatedMixin:
    """Mixin providing observer method on update balance event."""

    _notify: Callable[..., None]
    _update_data: Callable[..., None]

    def balance_updated(self, balance: str) -> None:
        """Handle the 'balance updated' event of User source."""
        self._update_data(balance=balance)
        self._notify('balance_updated', balance=balance)
