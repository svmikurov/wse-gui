"""Defines general application button."""

import toga

from wse.features.settings import BUTTON_HEIGHT, FONT_SIZE_APP


class AppButton(toga.Button):
    """General button."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the button."""
        super().__init__(*args, **kwargs)
        self.style.flex = 1
        self.style.height = BUTTON_HEIGHT
        self.style.font_size = FONT_SIZE_APP
