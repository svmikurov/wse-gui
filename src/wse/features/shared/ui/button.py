"""Defines general application button."""

from typing import Callable

import toga
from toga.style import Pack

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


class ButtonHandler:
    """Button event handler and Observer interaction."""

    def __init__(self, subject: ISubject) -> None:
        """Construct the handler."""
        self._subject = subject

    def button_press(self, button: toga.Button) -> None:
        """Handle button press and notify Subject."""
        self.subject.notify('handle_button', value=button.text)

    def keypad_press(self, button: toga.Button) -> None:
        """Handle keypad button press and notify Subject."""
        self.subject.notify('handel_keypad_press', value=button.text)

    def navigate(self, button: toga.Button) -> None:
        """Navigate to page, the button event listener."""
        self.subject.notify('navigate', nav_id=button.text)

    @property
    def subject(self) -> ISubject:
        """Subject of Observer pattern."""
        return self._subject


class ButtonFactory:
    """Factory for creating buttons with a single style."""

    @classmethod
    def create(
        cls,
        text: str | int = '',
        *,
        on_press: Callable[[toga.Button], None],
        style: Pack | None = None,
        **kwargs: object,
    ) -> toga.Button:
        """Create a button with default settings."""
        button = toga.Button(
            text=str(text),
            style=style if style is not None else Pack(),
            on_press=on_press,
            **kwargs,
        )
        return button
