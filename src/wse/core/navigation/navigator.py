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

    _CURRENT_NAV_ID_INDEX: Final[int] = -1
    _PREVIOUS_NAV_ID_INDEX: Final[int] = -2
    _NAV_IDS_NOT_FOR_HISTORY: set[NavigationID] = {
        NavigationID.LOGIN,
        NavigationID.LOGOUT,
    }

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
            content = self._get_content(nav_id)
        except KeyError:
            logger.error(f'The route for "{nav_id}" button is not set')
        else:
            self._set_window_content(content)
            self._add_to_history(nav_id)

    def _add_to_history(self, nav_id: NavigationID) -> None:
        if nav_id not in self._NAV_IDS_NOT_FOR_HISTORY:
            self._content_history.append(nav_id)

    # Utility methods
    def _get_content(self, nav_id: NavigationID) -> IContent | None:
        controller = self.routes[nav_id]
        # TODO: Remove next:
        # try:
        #     controller.request_context()
        # except AttributeError as e:
        #     logger.debug(f'Page has not `render_context` method: {e}')
        # TODO: Add next:
        # if hasattr(controller, 'request_context'):
        #     controller.request_context()
        return controller.content

    def _go_back(self) -> None:
        content = self._get_content(self._previous_nav_id)
        self._set_window_content(content)
        self._content_history.pop()

    def _set_window_content(self, content: IContent) -> None:
        self._main_window.content = content
        logger.debug(f'Navigated to "{content.id}" page')

    @property
    def _previous_nav_id(self) -> NavigationID | None:
        """Previous navigation ID (read-only)."""
        current_nav_id = self._retrieve_nav_id(self._CURRENT_NAV_ID_INDEX)
        previous_nav_id = self._retrieve_nav_id(self._PREVIOUS_NAV_ID_INDEX)

        if previous_nav_id == current_nav_id:
            self._PREVIOUS_NAV_ID_INDEX += self._CURRENT_NAV_ID_INDEX

        try:
            return self._retrieve_nav_id(self._PREVIOUS_NAV_ID_INDEX)
        except IndexError:
            logger.info('There are no visited pages in the stack')

    def _retrieve_nav_id(self, nav_index: int) -> NavigationID:
        return self._content_history[nav_index]
