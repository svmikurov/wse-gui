"""Defines the general button style and options."""

import toga
from toga import colors
from toga.widgets.base import StyleT

from wse.features.ui_config import UIStyle


class DisabledButtonMixin:
    """Custom button mixin."""

    enabled: bool
    style: StyleT

    def activate(self) -> None:
        """Activate the button (enable and reset styles)."""
        self.enabled = True
        del self.style.background_color
        del self.style.color

    def deactivate(self) -> None:
        """Deactivate the button (disable and apply styles)."""
        self.enabled = False
        self.style.background_color = colors.CADETBLUE
        self.style.color = colors.WHITE


class ButtonStyled(toga.Button):
    """General button with predefined styles."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Initialize the button with default styles."""
        super().__init__(*args, **kwargs)
        self._apply_default_styles()

    def _apply_default_styles(self) -> None:
        """Apply default styles to the button."""
        self.style.flex = 1
        self.style.height = UIStyle.BUTTON_HEIGHT
        self.style.font_size = UIStyle.BUTTON_FONT_SIZE
        self.style.padding = UIStyle.BUTTON_PADDING


class DisabledButton(DisabledButtonMixin, ButtonStyled):
    """Button with disabled state functionality."""
