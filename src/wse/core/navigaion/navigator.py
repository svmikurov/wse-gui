"""Defines a service for navigating through application pages."""

from __future__ import annotations

import logging
from collections import deque
from typing import TYPE_CHECKING, Final

import toga

from wse.core.settings import HISTORY_LEN
from wse.features.shared.button_text import ButtonText
from wse.interface.ifeatures import IContent

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from wse.application.app import WSE


class Navigator:
    """Application navigation service."""

    _PREVIOUS_CONTENT_INDEX: Final[int] = -2

    _app: WSE | None = None
    _main_window: toga.Window | None = None
    _content_history: deque[IContent]

    def __init__(self) -> None:
        """Construct the navigator."""
        self._content_history = deque(maxlen=HISTORY_LEN)

    def set_main_window(self, main_widow: toga.Window) -> None:
        """Set the application's main window for content display."""
        self._main_window = main_widow

    def set_app(self, app: WSE) -> None:
        """Set the application reference for feature access."""
        self._app = app

    @property
    def routes(self) -> dict[ButtonText, IContent | None]:
        """Routes to get page content to window content."""
        # The Features container provides the MVC model.
        features = self._app.features
        main = features.main
        foreign = features.foreign

        # Requesting page content from a page controller initializes
        # the MVC model components.
        # The page controller may contain additional logic to provide
        # page content.
        return {
            ButtonText.HOME: main.home_ctrl().content,
            ButtonText.FOREIGN: foreign.home_ctrl().content,
            ButtonText.FOREIGN_TASKS: foreign.tasks_ctrl().content,
            # To refactor
            ButtonText.FOREIGN_PARAMS: self._app.box_foreign_params,
            ButtonText.FOREIGN_EXERCISE: self._app.box_foreign_exercise,
            ButtonText.FOREIGN_CREATE: self._app.box_foreign_create,
            ButtonText.FOREIGN_UPDATE: self._app.box_foreign_update,
            ButtonText.GLOSSARY: self._app.box_glossary_main,
            ButtonText.MATHEM: self._app.box_mathematics_main,
            ButtonText.EXERCISES: None,
        }

    def navigate(self, button_text: ButtonText) -> None:
        """Navigate to page by button text value."""
        if button_text == ButtonText.BACK:
            self._go_back()
            return

        try:
            content = self.routes[button_text]
        except KeyError:
            logger.debug(f'The route for "{button_text}" button is not set')
        else:
            self._move_to(content)

    def _move_to(self, content: IContent) -> None:
        self._set_window_content(content)
        self._add_to_history(content)

    def _go_back(self) -> None:
        self._set_window_content(self._previous_content)
        self._content_history.pop()

    def _set_window_content(self, content: IContent) -> None:
        self._main_window.content = content
        logger.debug(f'Navigated to "{content.id}" content')

    def _add_to_history(self, content: IContent) -> None:
        self._content_history.append(content)

    @property
    def _previous_content(self) -> IContent | None:
        """Previous page content (read-only)."""
        try:
            return self._content_history[self._PREVIOUS_CONTENT_INDEX]
        except IndexError:
            logger.debug('No previous content in history')
            return None


navigator = Navigator()
