"""Mixins for navigation."""

from dataclasses import dataclass

from wse.core.interfaces import Navigable
from wse.core.navigation.nav_id import NavID
from wse.ui.base.navigate import NavigateABC


@dataclass
class NavigateStateMixin:
    """Mixin for State provides API for navigate."""

    _navigator: Navigable

    def navigate(self, nav_id: NavID, **kwargs: object) -> None:
        """Handle the navigate event.

        Parameters
        ----------
        nav_id : `NavID`
            The navigation route enumeration.
        **kwargs
            Additional keyword arguments:
            back_possible: `bool`, optional
                Conditions for the ability to return to the screen from
                which the navigation is made using navigation history
                (True by default)

        """
        self._navigator.navigate(nav_id=nav_id, **kwargs)


class NavigateViewMixin:
    """Mixin for View provides navigate feature."""

    _state: NavigateABC

    def navigate(self, nav_id: NavID) -> None:
        """Navigate."""
        self._state.navigate(nav_id)
