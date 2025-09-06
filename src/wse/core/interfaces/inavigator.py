"""Page navigation service."""

from typing import Any, Protocol, Type

import toga

from wse.apps.nav_id import NavID
from wse.feature.interfaces.imvc import PageControllerProto


class NavigatorProto(Protocol):
    """Page navigation service interface."""

    def navigate(self, nav_id: NavID, **kwargs: object) -> None:
        """Navigate to page."""

    def set_main_window(self, window: toga.Window) -> None:
        """Set main window."""

    def set_routes(
        self,
        routes: dict[NavID, Type[PageControllerProto[Any]]],
    ) -> None:
        """Set page route mapping."""
