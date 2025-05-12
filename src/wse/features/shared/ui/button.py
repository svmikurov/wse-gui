"""Defines general application button."""

import toga

from wse.features.settings import BUTTON_HEIGHT, FONT_SIZE_APP
from wse.interface.iobserver import ISubject


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
        self._subject.notify('handle_button_press', value=button.text)

    def keypad_press(self, button: toga.Button) -> None:
        """Handle keypad button press and notify Subject."""
        self._subject.notify('handle_keypad_press', value=button.text)

    def navigate(self, button: toga.Button) -> None:
        """Navigate to page, the button event listener."""
        self._subject.notify('navigate', nav_id=button.text)

    def add_listener(self, listener: object) -> None:
        """Add listener."""
        return self._subject.add_listener(listener)
