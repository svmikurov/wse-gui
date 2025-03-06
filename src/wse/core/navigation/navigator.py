"""Handles navigation between application screens."""

import toga

from wse.core.config import UIConfig
from wse.core.logger import setup_logger
from wse.core.navigation.routes import Route
from wse.interfaces.icore import INavigator

logger = setup_logger('navigator')


class Navigator(INavigator):
    """Manages navigation within the application."""

    def __init__(self, ui: UIConfig, main_window: toga.Window) -> None:
        """Construct the navigator."""
        self.main_window = main_window
        self.ui = ui

    def navigate(self, route: Route) -> None:
        """Navigate to the specified route."""
        screen = route.view
        self.main_window.content = screen
        logger.info(f'Navigating to {route.name}')
