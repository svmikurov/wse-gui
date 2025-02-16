"""General app text inputs."""

import toga
from toga.constants import CENTER

from wse.constants.settings import (
    TEXT_DISPLAY_FONT_SIZE,
    TEXT_DISPLAY_FONT_STYLE,
    TEXT_DISPLAY_PADDING,
    TITLE_LABEL_FONT_SIZE,
    TITLE_LABEL_PADDING,
)


class ValueListener:
    """Listener methods mixin."""

    value: str

    def change(self, value: str) -> None:
        """Update text widget value."""
        self.value = value

    def clean(self) -> None:
        """Clear the value of the text widget."""
        self.value = ''


class TitleLabel(toga.Label):
    """General title label."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the label."""
        super().__init__(*args, **kwargs)
        self.style.text_align = CENTER
        self.style.font_size = TITLE_LABEL_FONT_SIZE
        self.style.padding = TITLE_LABEL_PADDING


class LabelParam(toga.Label):
    """Styled label of exercise parameters."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the style of label."""
        super().__init__(*args, **kwargs)
        self.style.padding = (7, 0, 7, 2)


class ExerciseTextPanel(ValueListener, toga.MultilineTextInput):
    """Text panel for exercise info display."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the widget."""
        super().__init__(*args, **kwargs)
        self.readonly = True
        self.style.padding = TEXT_DISPLAY_PADDING
        self.style.font_size = TEXT_DISPLAY_FONT_SIZE
        self.style.font_style = TEXT_DISPLAY_FONT_STYLE


class InputTextField(ValueListener, toga.MultilineTextInput):
    """Text input field."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the widget."""
        super().__init__(*args, **kwargs)


class MultilineInfoPanel(ValueListener, toga.MultilineTextInput):
    """Text panel for info display."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the widget."""
        kwargs.setdefault('value', '')
        super().__init__(*args, **kwargs)
        self.style.flex = 1
        self.readonly = True


class UserInfoPanel(toga.Label):
    """User info panel."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the widget."""
        kwargs.setdefault('text', '')
        super().__init__(*args, **kwargs)
        self.style.flex = 1
        self.readonly = True
