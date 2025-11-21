"""Defines screen navigation service."""

from __future__ import annotations

import asyncio
import logging
from collections import deque
from typing import Any, Type

import toga
from injector import CallError, Injector, NoInject, inject

from wse.core.exceptions import (
    AuthError,
    NavigateError,
    RouteContentError,
)
from wse.core.navigation.nav_id import NavID
from wse.ui.base.view.abc import NavigableViewABC
from wse.ui.routes import UIRoutes

log = logging.getLogger(__name__)
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
        self._routes: dict[NavID, Type[NavigableViewABC[Any]]] = {}
        self._content_history: deque[NavID] = deque(maxlen=HISTORY_LEN)

        # Current view must contain method to manage the dependencies,
        # such as unsubscribe observer from subject
        self._current_screen: NavigableViewABC[Any] | None = None

    def set_main_window(self, window: toga.Window) -> None:
        """Set main window."""
        self._window = window

    def set_routes(
        self,
        routes: dict[NavID, Type[NavigableViewABC[Any]]],
    ) -> None:
        """Set screen route mapping."""
        self._routes = routes

    def navigate(self, nav_id: NavID, **kwargs: object) -> None:
        """Navigate to screen."""
        if nav_id == NavID.BACK:
            self._go_back()
            return

        try:
            self._update_window_content(nav_id)

        except AuthError:
            log.debug(f"Authentication required for '{nav_id.name}'")
            self._show_unauth_message()

        except RuntimeError:
            log.exception('Internal error\n')
            return

        except Exception as exc:
            print(f'{exc = }')
            self._show_server_error_message()
            log.error(f"Window content not updated with '{nav_id.name}'")
            return

        else:
            self._add_to_history(nav_id)

    def _update_window_content(self, nav_id: NavID) -> None:
        if self._window is None:
            log.error('Window is not initialized')
            raise

        try:
            screen = self._get_screen(nav_id)

        except Exception:
            log.error(f"No view to get content for '{nav_id.name}'")
            raise

        try:
            self._set_context(nav_id, screen)

        except Exception:
            raise

        else:
            self._window.content = screen.content
            self._close_current_screen()
            self._current_screen = screen

    def _get_view_type(self, nav_id: NavID) -> Type[NavigableViewABC[Any]]:
        if not self._routes:
            raise NavigateError('Route mapping is not initialized')
        try:
            return self._routes[nav_id]
        except KeyError as err:
            raise RouteContentError(err, nav_id, UIRoutes) from err

    def _get_screen(self, nav_id: NavID) -> NavigableViewABC[Any]:
        try:
            screen = self._injector.get(self._get_view_type(nav_id))

        except RouteContentError:
            log.exception(f"The navigation to the '{nav_id}' has failed")
            raise

        except CallError:
            log.exception('Dependency injection error:\n')
            raise

        except RuntimeError:
            log.error(f"Build '{nav_id}' runtime error")
            self._show_open_screen_error_message()
            raise

        except Exception:
            log.exception('Unexpected error:\n')
            raise

        else:
            return screen

    def _set_context(
        self,
        nav_id: NavID,
        new_view: NavigableViewABC[Any],
    ) -> None:
        try:
            new_view.on_open()

        except AttributeError:
            # The screen may not have any methods called when opened.
            pass

        except Exception:
            log.error(f"'{nav_id.name}' screen open error")
            raise

    def _close_current_screen(self) -> None:
        if self._current_screen:
            try:
                # The view object must have an on_close()
                # method with remove references to Subject,
                # such as unsubscribing from notifications.
                self._current_screen.on_close()
            except AttributeError:
                log.exception('Close screen error:\n')
            except Exception:
                log.exception('Unexpected error of close screen:\n')

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
            log.error(
                f'Attempt to get a previous screen from empty navigation '
                f"history on '{self._current_screen}' screen"
            )
            return

        try:
            self._update_window_content(nav_id)
        except Exception:
            return

    def _show_unauth_message(self) -> None:
        info_msg = toga.InfoDialog('Oops', 'Authentication required')
        if self._window:
            asyncio.create_task(self._window.dialog(info_msg))

    def _show_server_error_message(self) -> None:
        info_msg = toga.InfoDialog('Oops', 'Server error')
        if self._window:
            asyncio.create_task(self._window.dialog(info_msg))

    def _show_open_screen_error_message(self) -> None:
        info_msg = toga.InfoDialog('Oops', 'Open screen error')
        if self._window:
            asyncio.create_task(self._window.dialog(info_msg))