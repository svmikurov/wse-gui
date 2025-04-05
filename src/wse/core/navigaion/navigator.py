"""Defines a service for navigating through application pages."""

from __future__ import annotations

import logging
from collections import deque
from typing import TYPE_CHECKING

import toga

from wse.core.settings import HISTORY_LEN
from wse.features.shared.button_text import ButtonText
from wse.interface.ifeatures import IContent

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from wse.application import WSE


class Navigator:
    """Application navigation service."""

    PREVIOUS_PAGE_INDEX = -2

    app: WSE | None = None

    def __init__(self) -> None:
        """Construct the navigator."""
        self._main_window: toga.Window | None = None
        self._page_history = deque(maxlen=HISTORY_LEN)

    def set_main_window(self, main_widow: toga.Window) -> None:
        """Set application main window."""
        self._main_window = main_widow

    @classmethod
    def set_app(cls, app: WSE) -> None:
        """Set application."""
        cls._app = app

    @property
    def routes(self) -> dict:
        """Routes to get page content to window content."""
        # The Features container provides the MVC model.
        features = self._app.features

        # Requesting page content from a page controller initializes
        # the MVC model components.
        # The page controller may contain additional logic to provide
        # page content.
        return {
            ButtonText.HOME: features.main.home_ctrl().content,
            ButtonText.FOREIGN: features.foreign.foreign_ctrl().content,
            ButtonText.GLOSSARY: self._app.box_glossary_main,
            ButtonText.MATHEM: self._app.box_mathematics_main,
            ButtonText.EXERCISES: None,
            ButtonText.BACK: self.previous_content,
        }

    def navigate(self, button_text: ButtonText) -> None:
        """Navigate to page by button text value."""
        content = self.routes.get(button_text)
        if content:
            self._set_window_content(content)
            self._page_history.append(content)

    def _set_window_content(self, content: IContent) -> None:
        self._main_window.content = content

    @property
    def previous_content(self) -> IContent | None:
        """Previous page content (read-only)."""
        try:
            content = self._page_history[self.PREVIOUS_PAGE_INDEX]
        except IndexError:
            logger.debug('There is no a previous content')
        else:
            return content


navigator = Navigator()
