"""Defines page navigation service."""

from __future__ import annotations

import logging
from collections import deque
from typing import Any, Type

import toga
from injector import Injector, NoInject, inject

from wse.core.exceptions import ContentError, NavigateError
from wse.core.navigation.nav_id import NavID
from wse.feature.interfaces.imvc import PageControllerProto

logger = logging.getLogger(__name__)

HISTORY_LEN = 10


class Navigator:
    """Page navigation service."""

    _PREVIOUS_PAGE_INDEX = -1
    _EXCLUDE_HISTORY: set[NavID] = {
        NavID.LOGOUT,
    }

    @inject
    def __init__(
        self,
        injector: Injector,
        window: NoInject[toga.Window | None] = None,
    ) -> None:
        """Construct the navigator."""
        self._injector = injector
        self._window = window
        self._routes: dict[NavID, Type[PageControllerProto[Any]]] = {}
        self._content_history: deque[NavID] = deque(maxlen=HISTORY_LEN)

    def navigate(self, nav_id: NavID, **kwargs: object) -> None:
        """Navigate to page."""
        if nav_id == NavID.BACK:
            self._go_back()
            return

        try:
            self._update_window_content(nav_id, **kwargs)
        except (NavigateError, ContentError):
            logger.exception('Window content is not updated')
        else:
            self._add_to_history(nav_id)

    def _update_window_content(self, nav_id: NavID, **kwargs: object) -> None:
        if self._window is None:
            raise NavigateError('Window is not initialized')

        try:
            page_controller = self._injector.get(
                self._get_page_controller(nav_id)
            )
        except ContentError:
            logger.error(f"The navigation to the '{nav_id}' has failed")
            raise
        else:
            try:
                page_controller.on_open(**kwargs)
            except AttributeError:
                # The page may not have any methods called when opened.
                pass
            self._window.content = page_controller.content
            logger.debug(f"The '{nav_id}' is open")

    def set_main_window(self, window: toga.Window) -> None:
        """Set main window."""
        self._window = window

    def set_routes(
        self,
        routes: dict[NavID, Type[PageControllerProto[Any]]],
    ) -> None:
        """Set page route mapping."""
        self._routes = routes

    def _get_page_controller(
        self,
        nav_id: NavID,
    ) -> Type[PageControllerProto[Any]]:
        if self._routes is None:
            raise NavigateError('Route mapping is not initialized')

        try:
            return self._routes[nav_id]
        except KeyError as err:
            raise ContentError(
                f"Route mapping for '{nav_id}' to controller is not set"
            ) from err

    def _add_to_history(self, nav_id: NavID) -> None:
        """Add navigation ID to history."""
        if nav_id not in self._EXCLUDE_HISTORY:
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
