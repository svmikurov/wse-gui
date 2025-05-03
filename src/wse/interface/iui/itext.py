"""Defines protocol interfaces for text display."""

from typing import Protocol

import toga
from toga.style import Pack

from wse.features.shared.enums import UIName
from wse.interface.iobserver import ISubject

# ruff: noqa: D101, D102, D204, E301, E302
# fmt: off


class IDisplayPanel(Protocol):
    """Protocol defining the interface for button handler."""
    @property
    def content(self) -> [toga.Widget]:
        """Widgets of content."""
    def update_style(self, value: Pack) -> None:
        """Update display style."""
    def change(self, value: str) -> None:
        """Update text widget value."""
    def clean(self) -> None:
        """Clear the value of the text widget."""

class IDisplayModel(Protocol):
    """Protocol defining the interface for text display model."""
    _ui_name: UIName
    def set_ui_name(self, ui_name: UIName) -> None:
        """Set UI display name."""
    def change(self, value: str) -> None:
        """Change a text to display."""
    def clean(self) -> None:
        """Clean a text in display panel."""
    def _notify_change(self) -> None: ...
    @property
    def subject(self) -> ISubject:
        """Model subject."""
    @property
    def text(self) -> str:
        """Display model text."""
