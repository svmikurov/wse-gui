"""Page navigation service."""

from typing import Protocol, Type

import toga

from wse.core.navigation.nav_id import NavID
from wse.feature.interfaces.icontent import GetContentProto


class Navigable(Protocol):
    """Page navigation service interface."""

    def navigate(self, nav_id: NavID, **kwargs: object) -> None:
        """Navigate to page."""

    def set_main_window(self, window: toga.Window) -> None:
        """Set main window."""

    def set_routes(
        self,
        routes: dict[NavID, Type[GetContentProto]],
    ) -> None:
        """Set page route mapping."""
