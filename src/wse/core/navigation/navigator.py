"""Handles navigation between application screens."""

from __future__ import annotations

from collections import deque
from typing import TYPE_CHECKING

import toga

from wse.config.config import Settings
from wse.core.logger import setup_logger
from wse.core.navigation.routes import Route
from wse.interfaces.icore import INavigator

if TYPE_CHECKING:
    from wse.container import ApplicationContainer

logger = setup_logger('navigator')


class Navigator(INavigator):
    """Manages navigation within the application."""

    PREVIOUS_SCREEN_INDEX = -2

    def __init__(
        self,
        container: ApplicationContainer,
        settings: Settings,
    ) -> None:
        """Construct the navigator."""
        self.container = container
        self.history_len = settings.HISTORY_LEN
        self.screen_history = deque(maxlen=self.history_len)
        self.main_window = None

    def set_main_window(self, main_window: toga.Window) -> None:
        """Set main window to navigate."""
        self.main_window = main_window

    def navigate(self, route: Route) -> None:
        """Navigates to the specified route by creating a controller."""
        # Get a controller factory from a container
        feature = getattr(self.container, route.feature)
        controller_factory = getattr(feature, route.controller_factory)

        # Create a controller and get it View
        controller = controller_factory()
        self.main_window.content = controller.view
        logger.info(f'Navigating to {route.name}')
        self.screen_history.append(route)

    def back(self) -> None:
        """Move back screen."""
        if len(self.screen_history) >= 2:
            route = self.screen_history[self.PREVIOUS_SCREEN_INDEX]
            self.navigate(route)
