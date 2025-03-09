"""Handles navigation between application screens."""

from __future__ import annotations

from typing import TYPE_CHECKING

import toga

from wse.core.logger import setup_logger
from wse.core.navigation.routes import Route
from wse.interfaces.icore import INavigator

if TYPE_CHECKING:
    from wse.core.di_container import DIContainer

logger = setup_logger('navigator')


class Navigator(INavigator):
    """Manages navigation within the application."""

    def __init__(self, container: DIContainer) -> None:
        """Construct the navigator."""
        self.main_window = None
        self.container = container

    def set_main_window(self, main_window: toga.Window) -> None:
        """Set main window to navigate."""
        self.main_window = main_window

    def navigate(self, route: Route) -> None:
        """Navigates to the specified route by creating a controller."""
        # Get a controller factory from a container
        controller_factory = getattr(self.container, route.controller_factory)

        # Create a controller and get it View
        controller = controller_factory()
        self.main_window.content = controller.view
        logger.info(f'Navigating to {route.name}')
