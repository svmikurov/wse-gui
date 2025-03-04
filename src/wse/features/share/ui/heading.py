"""Screen heading."""

import toga
from toga.constants import CENTER


class Heading(toga.Label):
    """Screen heading."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Screen heading."""
        super().__init__(*args, **kwargs)
        self.style.text_align = CENTER
