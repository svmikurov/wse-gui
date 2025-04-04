"""Defines the application's relationship with features."""

import toga

from wse.features.shared.base import BaseContent


class AppHub:
    """Application's relationship with features."""

    def __init__(self, app: toga.App) -> None:
        """Construct the relationship."""
        self._app = app

    # Listener methods
    def set_window_content(self, content: BaseContent) -> None:
        """set main window content."""
        self._app.main_window.content = content
