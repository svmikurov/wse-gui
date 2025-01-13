"""General app text input."""

import toga
from toga.style import Pack
from travertino.constants import ITALIC

from wse.constants import (
    BUTTON_HEIGHT,
    FONT_SIZE_APP,
    TEXT_DISPLAY_FONT_SIZE,
    TEXT_DISPLAY_FONT_STYLE,
)


class TextInputApp(toga.TextInput):
    """Text input widget.

    Defines a common style for derived TextInput widgets.
    """

    def __init__(self, **kwargs: object) -> None:
        """Construct the widget."""
        super().__init__(**kwargs)
        self.style.flex = 1
        self.style.height = BUTTON_HEIGHT
        self.style.font_size = FONT_SIZE_APP

    def clean(self) -> None:
        """Clear the text input widget value."""
        self.value = None


class MulTextInpApp(toga.MultilineTextInput):
    """MultilineTextInput application widget."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the table."""
        super().__init__(*args, **kwargs)
        self.style.flex = 1
        self.style.padding = (2, 0, 2, 0)
        self.style.font_style = ITALIC

    def clean(self) -> None:
        """Clear the text input widget value."""
        self.value = None


class TextPanel(toga.MultilineTextInput):
    """Custom MultilineTextInput for info display."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the input."""
        super().__init__(*args, **kwargs)
        self.style.style = Pack(flex=1)
        self.style.readonly = True

    def change(self, text: str | None) -> None:
        """Update text widget value."""
        self.value = text

    def clean(self) -> None:
        """Clear the value of the text widget."""
        self.value = None


class TaskTextPanel(TextPanel):
    """Exercise text display widget."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the widget."""
        super().__init__(*args, **kwargs)
        self.style.padding = (0, 2, 0, 2)
        self.style.font_size = TEXT_DISPLAY_FONT_SIZE
        self.style.font_style = TEXT_DISPLAY_FONT_STYLE
