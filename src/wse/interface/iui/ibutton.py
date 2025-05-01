"""Defines protocol interfaces for user interfaces."""

from typing import Callable, Protocol

import toga

from wse.interface.ifeatures import ISubject

# ruff: noqa: D101, D102, D204, E301, E302
# fmt: off


class IButtonHandler(Protocol):
    """Protocol defining the interface for button handler."""
    def handle_button_press(self, button: toga.Button) -> None:
        """Handle button press and notify Subject."""
    @property
    def subject(self) -> ISubject:
        """Get the subject for observer pattern notifications."""

class IButtonFactory(Protocol):
    """Protocol defining the interface for button factory."""
    def create_button(
        self,
        text: str | int,
        on_press: Callable[[toga.Button], None],
        **kwargs: object,
    ) -> toga.Button:
        """Create a button with default settings."""
