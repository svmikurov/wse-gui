"""Defines a heading widget for screens."""

import toga
from toga.constants import CENTER


class Heading(toga.Label):
    """Represents a heading for application screens."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the heading."""
        super().__init__(*args, **kwargs)
        self.style.text_align = CENTER
