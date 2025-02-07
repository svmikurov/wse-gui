"""General app text inputs."""

import toga

from wse.constants import (
    TEXT_DISPLAY_FONT_SIZE,
    TEXT_DISPLAY_FONT_STYLE,
    TEXT_DISPLAY_PADDING,
)


class ListenerMixin:
    """Listener methods mixin."""

    value: str

    def change(self, text: str) -> None:
        """Update text widget value."""
        self.value = text

    def clean(self) -> None:
        """Clear the value of the text widget."""
        self.value = ''


class InfoTextPanel(ListenerMixin, toga.MultilineTextInput):
    """Text panel for info display."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the widget."""
        super().__init__(*args, **kwargs)
        self.readonly = True


class ExerciseTextPanel(ListenerMixin, toga.MultilineTextInput):
    """Text panel for exercise info display."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the widget."""
        super().__init__(*args, **kwargs)
        self.readonly = True
        self.style.padding = TEXT_DISPLAY_PADDING
        self.style.font_size = TEXT_DISPLAY_FONT_SIZE
        self.style.font_style = TEXT_DISPLAY_FONT_STYLE


class InfoPanel(toga.MultilineTextInput):
    """Text panel for info display."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the widget."""
        super().__init__(*args, **kwargs)
        self.style.flex = 1
        self.readonly = True


class InputTextField(ListenerMixin, toga.MultilineTextInput):
    """Text input field."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the widget."""
        super().__init__(*args, **kwargs)


class UserInfoPanel(toga.Label):
    """User info panel."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the widget."""
        kwargs.setdefault('text', '')
        super().__init__(*args, **kwargs)
        self.style.flex = 1
        self.readonly = True
