"""Defines a heading widget for screens."""

import toga
from toga.constants import CENTER

from wse.features.ui_config import UIStyle


class Heading(toga.Label):
    """Represents a heading for application screens."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Initialize the heading with default styles."""
        super().__init__(*args, **kwargs)
        self._apply_default_styles()

    def _apply_default_styles(self) -> None:
        """Apply default styles to the heading."""
        self.style.text_align = CENTER
        self.style.font_size = UIStyle.HEADING_FONT_SIZE
        self.style.height = UIStyle.HEADING_HEIGHT
        self.style.padding = UIStyle.HEADING_PADDING
