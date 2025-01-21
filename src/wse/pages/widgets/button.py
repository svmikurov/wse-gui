"""General app buttons."""

import toga
from toga import colors
from toga.widgets.base import StyleT

from wse.constants import BUTTON_HEIGHT, FONT_SIZE_APP


class ButtonMixin:
    """Custom button mixin."""

    enabled: bool
    style: StyleT

    def activate(self) -> None:
        """Activate the bottom."""
        self.enabled = True
        del self.style.background_color
        del self.style.color

    def deactivate(self) -> None:
        """Activate the bottom."""
        self.enabled = False
        self.style.background_color = colors.rgb(32, 32, 32)
        self.style.color = colors.WHITE


class BtnApp(toga.Button):
    """General button."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the button."""
        super().__init__(*args, **kwargs)
        self.style.flex = 1
        self.style.height = BUTTON_HEIGHT
        self.style.font_size = FONT_SIZE_APP


class SmBtn(toga.Button):
    """Small button."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the button."""
        super().__init__(*args, **kwargs)
        self.style.flex = 1
        self.style.height = 45


class AnswerBtn(ButtonMixin, toga.Button):
    """User answer button."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the button."""
        super().__init__(*args, **kwargs)
        self.style.flex = 1
        self.style.height = 100
        self.style.font_size = 9
