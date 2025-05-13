"""Defines protocol interfaces for text display."""

from typing import Protocol

import toga
from toga.style import Pack

from wse.features.shared.enums import FieldID
from wse.interfaces.iobserver import ISubject

# fmt: off


class IDisplayPanel(Protocol):
    """Protocol defining the interface for button handler."""
    @property
    def content(self) -> [toga.Widget]:
        """Widgets of content."""
    @property
    def text(self) -> str:
        """Text on display."""
    def update_style(self, value: Pack) -> None:
        """Update display style."""
    def change(self, value: str) -> None:
        """Update text widget value."""
    def clean(self) -> None:
        """Clear the value of the text widget."""

class IDisplayModel(Protocol):
    """Protocol defining the interface for text display model."""
    _event: FieldID
    def change(self, value: str) -> None:
        """Change a text to display."""
    def clean(self) -> None:
        """Clean a text in display panel."""
    def _notify_change(self) -> None: ...
    def _notify_clean(self) -> None: ...
    @property
    def subject(self) -> ISubject:
        """Model subject."""
    @property
    def text(self) -> str:
        """Display model text."""
    def subscribe(self, field: FieldID, listener: object) -> None:
        """Set UI display name with model listener."""
