"""Defines page navigation service."""

import logging

import toga

from wse.features.exceptions import ContentError, NavigateError
from wse.features.interfaces.icontent import IContent
from wse.features.interfaces.imvc import IPageController
from wse.features.subapps.nav_id import NavID

logger = logging.getLogger('__name__')


class Navigator:
    """Page navigation service."""

    def __init__(
        self,
        window: toga.Window | None = None,
        routes: dict[NavID, IPageController] | None = None,
    ) -> None:
        """Construct the navigator."""
        self._window = window
        self._routes = routes

    def navigate(self, nav_id: NavID) -> None:
        """Navigate to page."""
        if self._window is None:
            raise NavigateError('Window is not initialized')

        try:
            content = self._get_content(nav_id)
        except ContentError:
            logger.exception(f'Failed to navigate to "{nav_id}"')
        else:
            self._window.content = content
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
