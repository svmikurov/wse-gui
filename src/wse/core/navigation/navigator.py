"""Defines page navigation service."""

import logging

import toga

from wse.features.exeptions import ContentError, NavigateError
from wse.features.interfaces import IController
from wse.features.interfaces.icontent import IContent
from wse.features.subapps.nav_id import NavID

logger = logging.getLogger('wse')


class Navigator:
    """Page navigation service."""

    _fallback_page_id = NavID.HOME

    def __init__(
        self,
        window: toga.Window | None = None,
        routes: dict[NavID, IController] | None = None,
    ) -> None:
        """Construct the navigator."""
        self._window = window
        self._routes = routes

    def navigate(self, nav_id: NavID) -> None:
        """Navigate to page."""
        try:
            content = self._get_content(nav_id)

        except ContentError:
            try:
                content = self._get_content(self._fallback_page_id)

            except ContentError as err:
                raise NavigateError('Failed to navigate to fallback') from err

        if self._window is None:
            raise NavigateError('Window is not initialized')

        self._window.content = content
        logger.debug(f'Window content updated for ID: "{nav_id}"')

    def set_main_window(self, window: toga.Window) -> None:
        """Set main window."""
        self._window = window

    def set_routes(self, routes: dict[NavID, IController]) -> None:
        """Set page route mapping."""
        self._routes = routes

    def _get_content(self, nav_id: NavID) -> IContent:
        if self._routes is None:
            raise NavigateError('Route mapping is not initialized')

        try:
            return self._routes[nav_id].content
        except KeyError as err:
            raise ContentError(f'Failed to navigate: "{nav_id}"') from err
