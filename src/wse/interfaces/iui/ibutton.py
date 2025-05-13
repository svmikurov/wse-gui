"""Defines protocol interfaces for user interfaces."""

from typing import Callable, Protocol

import toga
from toga.style import Pack

# fmt: off


class IButtonHandler(Protocol):
    """Protocol defining the interface for button handler."""
    def add_listener(self, listener: object) -> None:
        """Add listener."""
    def button_press(self, button: toga.Button) -> None:
        """Handle button press and notify Subject."""
    def keypad_press(self, button: toga.Button) -> None:
        """Handle keypad button press and notify Subject."""
    def navigate(self, button: toga.Button) -> None:
        """Navigate by button text, button handler."""

class IButtonFactory(Protocol):
    """Protocol defining the interface for button factory."""
    @classmethod
    def create(
        cls,
        text: str | int = '',
        *,
        on_press: Callable[[toga.Button], None],
        style: Pack | None = None,
        **kwargs: object,
    ) -> toga.Button:
        """Create a button with default settings."""
