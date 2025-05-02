"""Defines protocol interfaces for user interfaces."""

from typing import Callable, Protocol

import toga
from toga.style import Pack

from wse.interface.ifeatures import ISubject

# ruff: noqa: D101, D102, D204, E301, E302
# fmt: off


class IButtonHandler(Protocol):
    """Protocol defining the interface for button handler."""
    @property
    def subject(self) -> ISubject:
        """Get the subject for observer pattern notifications."""
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
