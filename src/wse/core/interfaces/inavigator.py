"""Page navigation service."""

from typing import Protocol

import toga

from wse.features.interfaces import IController
from wse.features.subapps.nav_id import NavID


class INavigator(Protocol):
    """Page navigation service interface."""

    def navigate(self, nav_id: NavID) -> None:
        """Navigate to page."""

    def set_main_window(self, window: toga.Window) -> None:
        """Set main window."""

    def set_routes(self, routes: dict[NavID, IController]) -> None:
        """Set page route mapping."""
