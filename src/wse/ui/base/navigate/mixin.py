"""Mixins for navigation."""

from dataclasses import dataclass

from wse.core.interfaces import Navigable
from wse.core.navigation.nav_id import NavID
from wse.ui.base.navigate import NavigateABC


@dataclass
class NavigateStateMixin:
    """Mixin for State provides API for navigate."""

    _navigator: Navigable

    def navigate(self, nav_id: NavID) -> None:
        """Handle the navigate event."""
        self._navigator.navigate(nav_id=nav_id)


class NavigateViewMixin:
    """Mixin for View provides navigate feature."""

    _state: NavigateABC

    def navigate(self, nav_id: NavID) -> None:
        """Navigate."""
        self._state.navigate(nav_id)
