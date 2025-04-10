"""Defines a service for navigating through application pages."""

import logging
from collections import deque
from typing import Final

import toga

from wse.core.navigation.navigation_id import NavigationID
from wse.core.settings import HISTORY_LEN
from wse.interface.ifeatures import IContent, IController

logger = logging.getLogger(__name__)


class Navigator:
    """Application navigation service."""

    _PREVIOUS_NAV_Id_INDEX: Final[int] = -2

    _main_window: toga.Window
    _routes: dict[NavigationID, IController]
    _content_history: deque[NavigationID]

    def __init__(self) -> None:
        """Construct the navigator."""
        self._content_history = deque(maxlen=HISTORY_LEN)

    def set_main_window(self, main_widow: toga.Window) -> None:
        """Set the application's main window for content display."""
        self._main_window = main_widow

    @property
    def routes(self) -> dict[NavigationID, IController]:
        """Routes to get page content to window content."""
        return self._routes

    @routes.setter
    def routes(self, value: dict[NavigationID, IController]) -> None:
        self._routes = value
        self._set_listener()

    def _set_listener(self) -> None:
        """Set navigator as view controller listener."""
        for _, controller in self.routes.items():
            controller.subject.add_listener(self)

    # Listener methods
    def navigate(self, nav_id: NavigationID) -> None:
        """Navigate to page by button text value."""
        if nav_id == NavigationID.BACK:
            self._go_back()
            return

        try:
            content = self._get_content(nav_id)
        except KeyError:
            logger.debug(f'The route for "{nav_id}" button is not set')
        else:
            self._set_window_content(content)
            self._content_history.append(nav_id)

    # Utility methods
    def _get_content(self, nav_id: NavigationID) -> IContent:
        return self.routes[nav_id].content

    def _go_back(self) -> None:
        content = self._get_content(self._previous_nav_id)
        self._set_window_content(content)
        self._content_history.pop()

    def _set_window_content(self, content: IContent) -> None:
        self._main_window.content = content
        logger.debug(f'Navigated to "{content.id}" content')

    @property
    def _previous_nav_id(self) -> NavigationID | None:
        """Previous navigation ID (read-only)."""
        try:
            nav_id = self._content_history[self._PREVIOUS_NAV_Id_INDEX]
            return nav_id
        except IndexError:
            return None
