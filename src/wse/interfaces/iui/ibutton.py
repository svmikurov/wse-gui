"""Defines protocol interfaces for user interfaces."""

from typing import Protocol

import toga

# fmt: off


class _IButtonHandler(Protocol):
    """Base protocol for button handlers with listener support."""
    def add_listener(self, listener: object) -> None:
        """Register an event listener."""

class IPressButtonHandler(_IButtonHandler):
    """Protocol for handlers processing button press events."""
    def handle_button_press(self, button: toga.Button) -> None:
        """Handle button press and notify observers."""

class INavigateButtonHandler(_IButtonHandler):
    """Protocol for handlers processing navigation events."""
    def navigate(self, button: toga.Button) -> None:
        """Handle navigation event and notify observers."""

class IComboButtonHandler(IPressButtonHandler, INavigateButtonHandler):
    """Combined protocol handling both press and navigation events."""
