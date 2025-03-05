"""Application navigation."""

import toga

from wse.core.config import UIConfig
from wse.core.navigation.routes import Route


class Navigator:
    """Application navigation."""

    def __init__(self, ui: UIConfig, main_window: toga.Window) -> None:
        """Construct the navigator."""
        self.main_window = main_window
        self.ui = ui

    def navigate(self, route: Route) -> None:
        """Navigate by route."""
        screen = route.view
        self.main_window.content = screen
