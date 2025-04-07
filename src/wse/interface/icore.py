"""Defines protocol interfaces for application components."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

import toga

from wse.interface.ifeatures import IController

if TYPE_CHECKING:
    from wse.core.navigation.navigation_id import NavigationID


class INavigator(Protocol):
    """Protocol defining the interface for navigator."""

    def navigate(self, navigation_id: NavigationID) -> None:
        """Navigate to page by navigation ID."""

    def set_main_window(self, main_widow: toga.Window) -> None:
        """Set the application's main window for content display."""

    @property
    def routes(self) -> dict[NavigationID, IController]:
        """Routes to get page content to window content."""

    @routes.setter
    def routes(self, value: dict[NavigationID, IController]) -> None: ...
