"""Defines a service for navigating through application pages."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

import toga

from wse.features.shared.button_names import ButtonText

logging.basicConfig(
    level=logging.DEBUG,
    format=f'[%(asctime)s] [%(name)s] [%(levelname)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from wse.application import WSE


class Navigator:
    """Application navigation service."""

    app: WSE | None = None

    def __init__(self) -> None:
        """Construct the navigator."""
        self._main_window: toga.Window | None = None

    def set_main_window(self, main_widow: toga.Window) -> None:
        """Set application main window."""
        self._main_window = main_widow
        logger.debug(f'Main_window: {self._main_window}')

    @classmethod
    def set_app(cls, app: WSE) -> None:
        """Set application."""
        cls.app = app
        logger.debug(f'App: {cls.app}')

    @property
    def routes(self) -> dict:
        return {
            ButtonText.FOREIGN_HOME: self.app.box_foreign_main,
            ButtonText.GLOSSARY_HOME: self.app.box_glossary_main,
            ButtonText.MATHEM_HOME: self.app.box_mathematics_main,
            ButtonText.EXERCISES_HOME: None,
        }

    def navigate(self, button_text: ButtonText) -> None:
        content = self.routes.get(button_text)
        if content:
            self._main_window.content = content


navigator = Navigator()
