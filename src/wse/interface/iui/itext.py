"""Defines protocol interfaces for text display."""

from typing import Protocol

import toga
from toga.style import Pack

# ruff: noqa: D101, D102, D204, E301, E302
# fmt: off


class IDisplay(Protocol):
    """Protocol defining the interface for button handler."""
    @property
    def content(self) -> [toga.Widget]:
        """Widgets of content."""
    def update_style(self, value: Pack) -> None:
        """Update display style."""
