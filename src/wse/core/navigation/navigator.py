"""Defines page navigation service."""

import logging
from collections import deque

import toga

from wse.features.exceptions import ContentError, NavigateError
from wse.features.interfaces.icontent import IContent
from wse.features.interfaces.imvc import IPageController
from wse.features.subapps.nav_id import NavID

logger = logging.getLogger('__name__')

HISTORY_LEN = 10


class Navigator:
    """Page navigation service."""

    _routes: dict[NavID, IPageController]

    _NAV_IDS_NOT_FOR_HISTORY: set[NavID] = {
        NavID.LOGIN,
        NavID.LOGOUT,
    }

    def __init__(self, window: toga.Window | None = None) -> None:
        """Construct the navigator."""
        self._window = window
        self._content_history: deque[NavID] = deque(maxlen=HISTORY_LEN)

    def navigate(self, nav_id: NavID) -> None:
        """Navigate to page."""
        if self._window is None:
            raise NavigateError('Window is not initialized')

        if nav_id == NavID.BACK:
            self._go_back()
            return

        try:
            content = self._get_content(nav_id)
        except ContentError:
            logger.exception(f'Failed to navigate to "{nav_id}"')
        else:
            self._window.content = content
            self._add_to_history(nav_id)
            logger.debug(f'Window content updated for ID: "{nav_id}"')

    def set_main_window(self, window: toga.Window) -> None:
        """Set main window."""
        self._window = window

    def set_routes(self, routes: dict[NavID, IPageController]) -> None:
        """Set page route mapping."""
        self._routes = routes

    def _get_content(self, nav_id: NavID) -> IContent:
        if self._routes is None:
            raise NavigateError('Route mapping is not initialized')

        try:
            return self._routes[nav_id].content
        except KeyError as err:
            raise ContentError(f'Failed to navigate: "{nav_id}"') from err

    def _add_to_history(self, nav_id: NavID) -> None:
        """Add navigation ID to history."""
        if nav_id not in self._NAV_IDS_NOT_FOR_HISTORY:
            self._content_history.append(nav_id)

    def _go_back(self) -> None:
        """Move on previous page."""
        # Remove current navigation ID from history
        self._content_history.pop()

        try:
            # Retrieve previous navigation id from history
            nav_id = self._content_history.pop()
        except IndexError:
            logger.debug('No previous page back button')
        else:
            self.navigate(nav_id)
