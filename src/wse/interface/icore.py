"""Defines protocol interfaces for application components."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

import toga

from wse.interface.ifeatures import IController

if TYPE_CHECKING:
    from wse.features.shared.button_text import ButtonText


class INavigator(Protocol):
    """Protocol defining the interface for navigator."""

    def navigate(self, button_text: ButtonText) -> None:
        """Navigate to page by button text."""

    def set_main_window(self, main_widow: toga.Window) -> None:
        """Set the application's main window for content display."""

    @property
    def routes(self) -> dict[ButtonText, IController]:
        """Routes to get page content to window content."""

    @routes.setter
    def routes(self, value: dict[ButtonText, IController]) -> None:
        pass