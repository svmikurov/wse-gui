"""Defines screen navigation service."""

from __future__ import annotations

import logging
from collections import deque
from typing import Any, Type

import toga
from injector import Injector, NoInject, inject

from wse.core.exceptions import ContentError, NavigateError
from wse.core.navigation.nav_id import NavID
from wse.feature.interfaces.imvc import NavigableView

logger = logging.getLogger(__name__)

audit = logging.getLogger('audit')


HISTORY_LEN = 10


class Navigator:
    """Screen navigation service."""

    _PREVIOUS_SCREEN_INDEX = -1
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
        self._routes: dict[NavID, Type[NavigableView[Any]]] = {}
        self._content_history: deque[NavID] = deque(maxlen=HISTORY_LEN)

        # Current view must contain method to manage the dependencies,
        # such as unsubscribe observer from subject
        self._current_view: NavigableView[Any] | None = None

    def navigate(self, nav_id: NavID, **kwargs: object) -> None:
        """Navigate to screen."""
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
            # The injector creates a view instance
            # that is hashed as the current one.
            new_view = self._injector.get(self._get_view_type(nav_id))

        except ContentError:
            logger.error(f"The navigation to the '{nav_id}' has failed")
            raise

        else:
            if self._current_view is None:
                audit.info('Current view was not set')

            else:
                try:
                    # The view object must have an on_close()
                    # method with remove references to itself,
                    # such as unsubscribing from notifications.
                    self._current_view.on_close()
                except AttributeError as err:
                    logger.exception('Close screen error:\n %s', err)

            try:
                new_view.on_open(**kwargs)

            except AttributeError:
                # The screen may not have any
                # methods called when opened.
                audit.info(f'Have no `on_open()`: {new_view.__class__}')

            self._window.content = new_view.content

            # Hash of the created view instance.
            self._current_view = new_view

    def set_main_window(self, window: toga.Window) -> None:
        """Set main window."""
        self._window = window

    def set_routes(
        self,
        routes: dict[NavID, Type[NavigableView[Any]]],
    ) -> None:
        """Set screen route mapping."""
        self._routes = routes

    def _get_view_type(self, nav_id: NavID) -> Type[NavigableView[Any]]:
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
        """Move on previous screen."""
        # Remove current navigation ID from history
        self._content_history.pop()

        try:
            # Get previous navigation id from history
            nav_id = self._content_history[self._PREVIOUS_SCREEN_INDEX]
        except IndexError:
            logger.debug('No previous screen back button')
        else:
            self._update_window_content(nav_id)
