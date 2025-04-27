"""Defines general application button."""

from typing import Callable

import toga

from wse.features.settings import BUTTON_HEIGHT, FONT_SIZE_APP
from wse.interface.ifeatures import ISubject


class AppButton(toga.Button):
    """General button."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the button."""
        super().__init__(*args, **kwargs)
        self.style.flex = 1
        self.style.height = BUTTON_HEIGHT
        self.style.font_size = FONT_SIZE_APP


class KeypadButton(toga.Button):
    """Button of keypad."""

    _FONT_SIZE = 18
    _BUTTON_HEIGHT = 80
    _BUTTON_PADDING = (0, 0, 0, 0)

    def __init__(
        self,
        text: str | int,
        *,
        font_size: int = _FONT_SIZE,
        button_height: int = _BUTTON_HEIGHT,
        padding: tuple = _BUTTON_PADDING,
        on_press: Callable[[toga.Button], None],
        **kwargs: object,
    ) -> None:
        """Construct the button."""
        super().__init__(text=str(text), **kwargs)
        self.style.font_size = font_size
        self.style.flex = 1
        self.style.height = button_height
        self.on_press = on_press
        self.style.padding = padding


class ButtonHandler:
    """Button event handler and Observer interaction."""

    def __init__(self, subject: ISubject) -> None:
        """Construct the handler."""
        self._subject = subject

    def handle_button_press(self, button: toga.Button) -> None:
        """Handle button press and notify Subject."""
        self.subject.notify('handle_button', value=button.text)

    @property
    def subject(self) -> ISubject:
        """Subject of Observer pattern."""
        return self._subject


class ButtonFactory:
    """Factory for creating buttons with a single style."""

    _DEFAULT_FONT_SIZE = 18
    _DEFAULT_HEIGHT = 80
    _DEFAULT_PADDING = (0, 0, 0, 0)

    def create_button(
        self,
        text: str | int,
        on_press: Callable[[toga.Button], None],
        **kwargs: object,
    ) -> toga.Button:
        """Create a button with default settings."""
        button = KeypadButton(
            text=str(text),
            on_press=on_press,
            font_size=self._DEFAULT_FONT_SIZE,
            button_height=self._DEFAULT_HEIGHT,
            padding=self._DEFAULT_PADDING,
            **kwargs,
        )
        return button
