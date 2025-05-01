"""Defines general application button."""

from functools import cached_property
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

    def handle_button_press(self, button: toga.Button) -> None:
        """Handle button press and notify Subject."""
        self.subject.notify('handle_button', value=button.text)

    @property
    def subject(self) -> ISubject:
        """Subject of Observer pattern."""
        return self._subject


class ButtonFactory:
    """Factory for creating buttons with a single style."""

    def __init__(
        self,
        style_config: dict,
        style_id: str,
    ) -> None:
        """Construct the button."""
        self._style_config = style_config
        self._style_id = style_id

    def create_button(
        self,
        text: str | int,
        on_press: Callable[[toga.Button], None],
        style: Pack | None = None,
        **kwargs: object,
    ):
        """Create a button with default settings."""
        button = toga.Button(
            text=str(text),
            on_press=on_press,
            style=style if style is not None else self._button_style,
            **kwargs,
        )
        return button

    @cached_property
    def _button_style(self) -> Pack:
        """Get button style."""
        return Pack(**self._style_config.get(self._style_id))
