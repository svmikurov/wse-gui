"""Handles navigation between application screens."""

import toga

from wse.core.logger import setup_logger
from wse.core.navigation.routes import Route
from wse.interfaces.icore import INavigator

logger = setup_logger('navigator')


class Navigator(INavigator):
    """Manages navigation within the application."""

    def __init__(self) -> None:
        """Construct the navigator."""
        self.main_window = None

    def set_main_window(self, main_window: toga.Window) -> None:
        """Set main window to navigate."""
        self.main_window = main_window

    def navigate(self, route: Route) -> None:
        """Navigate to the specified route."""
        content = route.view()
        self.main_window.content = content
        logger.info(f'Navigating to {route.name}')
