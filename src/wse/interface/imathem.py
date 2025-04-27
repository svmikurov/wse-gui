"""Defines protocol interfaces for mathematical features components."""

from typing import Protocol

import toga


class INumericScreen(Protocol):
    """Protocol defining the interface for numeric screen."""

    @property
    def widgets(self) -> list[toga.Widget]:
        """Widgets to unpack into general container."""


class INumericKeypad(Protocol):
    """Protocol defining the interface for numeric keypad."""

    @property
    def keypad_v1(self) -> [toga.Widget]:
        """Widgets of numeric keypad."""


class IButtonBox(Protocol):
    """Protocol defining the interface for buttons box."""

    @property
    def content(self) -> [toga.Widget]:
        """Widgets of buttons box."""


class IKeypadButton(Protocol):
    """Protocol defining the interface for keypad button."""
