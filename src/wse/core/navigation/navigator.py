"""Defines page navigation service."""

import logging
from collections import deque

import toga
from typing_extensions import override

from wse.core.exceptions import ContentError, NavigateError
from wse.core.interfaces import INavigator
from wse.features.interfaces.imvc import IPageController
from wse.features.subapps.nav_id import NavID

logger = logging.getLogger(__name__)

HISTORY_LEN = 10


class Navigator(INavigator):
    """Page navigation service."""

    _routes: dict[NavID, IPageController]

    _PREVIOUS_PAGE_INDEX = -1
    _NAV_IDS_NOT_FOR_HISTORY: set[NavID] = {
        NavID.LOGOUT,
    }

    def __init__(self, window: toga.Window | None = None) -> None:
        """Construct the navigator."""
        self._window = window
        self._content_history: deque[NavID] = deque(maxlen=HISTORY_LEN)

    @override
    def navigate(self, nav_id: NavID, **kwargs: object) -> None:
        """Navigate to page."""
        if nav_id == NavID.BACK:
            self._go_back()
            return

        self._update_window_content(nav_id, **kwargs)
        self._add_to_history(nav_id)

    def _update_window_content(self, nav_id: NavID, **kwargs: object) -> None:
        if self._window is None:
            raise NavigateError('Window is not initialized')

        try:
            page_controller = self._get_page_controller(nav_id)
        except ContentError:
            logger.exception(f'Failed to navigate to "{nav_id}"')
        else:
            page_controller.on_open(**kwargs)
            self._window.content = page_controller.content
            logger.debug(f"The '{nav_id}' page is open")

    @override
    def set_main_window(self, window: toga.Window) -> None:
        """Set main window."""
        self._window = window

    @override
    def set_routes(self, routes: dict[NavID, IPageController]) -> None:
        """Set page route mapping."""
        self._routes = routes

    def _get_page_controller(self, nav_id: NavID) -> IPageController:
        if self._routes is None:
            raise NavigateError('Route mapping is not initialized')

        try:
            return self._routes[nav_id]
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
            # Get previous navigation id from history
            nav_id = self._content_history[self._PREVIOUS_PAGE_INDEX]
        except IndexError:
            logger.debug('No previous page back button')
        else:
            self._update_window_content(nav_id)
