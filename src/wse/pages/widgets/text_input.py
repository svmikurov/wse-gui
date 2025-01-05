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
        style = Pack(
            padding=(0, 0, 0, 0),
            height=BUTTON_HEIGHT,
            font_size=FONT_SIZE_APP,
        )
        kwargs['style'] = kwargs.get('style', style)
        super().__init__(**kwargs)

    def clean(self) -> None:
        """Clear the text input widget value."""
        self.value = None


class MulTextInpApp(toga.MultilineTextInput):
    """MultilineTextInput application widget."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the table."""
        style = Pack(
            padding=(2, 0, 2, 0),
            font_style=ITALIC,
        )
        kwargs['style'] = kwargs.get('style', style)
        super().__init__(*args, **kwargs)

    def clean(self) -> None:
        """Clear the text input widget value."""
        self.value = None


class TextPanel(toga.MultilineTextInput):
    """Exercise text display widget."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the widget."""
        super().__init__(*args, **kwargs)
        self.style.flex = 1
        self.style.padding = (0, 2, 0, 2)
        self.style.font_size = TEXT_DISPLAY_FONT_SIZE
        self.style.font_style = TEXT_DISPLAY_FONT_STYLE
        self.readonly = True

    def change(self, text: str | None) -> None:
        """Update text widget value."""
        self.value = text

    def clean(self) -> None:
        """Clear the value of the text widget."""
        self.value = ''
