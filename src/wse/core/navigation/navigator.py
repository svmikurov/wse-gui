"""Defines a service for navigating through application pages."""

import logging
from collections import deque
from typing import Final

import toga

from wse.core.navigation.navigation_id import NavigationID
from wse.interface.ifeatures import IContent, IContextController, IController

logger = logging.getLogger(__name__)


class Navigator:
    """Application navigation service."""

    _PREVIOUS_NAV_Id_INDEX: Final[int] = -2

    _main_window: toga.Window
    _routes: dict[NavigationID, IController | IContextController]
    _content_history: deque[NavigationID]

    def __init__(self, history_len: int) -> None:
        """Construct the navigator."""
        self._content_history = deque(maxlen=history_len)

    def set_main_window(self, main_widow: toga.Window) -> None:
        """Set the application's main window for content display."""
        self._main_window = main_widow

    @property
    def routes(self) -> dict[NavigationID, IController | IContextController]:
        """Routes to get page content to window content."""
        return self._routes

    @routes.setter
    def routes(
        self, value: dict[NavigationID, IController | IContextController]
    ) -> None:
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
            context = self._request_context(nav_id)
        except KeyError:
            logger.error(f'The route for "{nav_id}" button is not set')
        else:
            self._set_window_content(context)
            self._content_history.append(nav_id)

    # Utility methods
    def _request_context(self, nav_id: NavigationID) -> IContent | None:
        controller = self.routes[nav_id]
        try:
            controller.request_context()
        except AttributeError as e:
            logger.debug(f'Page has not `render_context` method: {e}')
        return controller.content

    def _go_back(self) -> None:
        content = self._request_context(self._previous_nav_id)
        self._set_window_content(content)
        self._content_history.pop()

    def _set_window_content(self, content: IContent) -> None:
        self._main_window.content = content
        logger.debug(f'Navigated to "{content.id}" page')

    @property
    def _previous_nav_id(self) -> NavigationID | None:
        """Previous navigation ID (read-only)."""
        try:
            nav_id = self._content_history[self._PREVIOUS_NAV_Id_INDEX]
            return nav_id
        except IndexError:
            return None
