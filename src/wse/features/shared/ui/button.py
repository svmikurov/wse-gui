"""Provides general application button components and event handlers.

This module contains:
- AppButton - A styled button for the application
- Button event handlers with different behaviors (press/navigate)
- Mixin classes for button functionality
"""

import toga

from wse.features.settings import BUTTON_HEIGHT, FONT_SIZE_APP
from wse.interfaces.iobserver import ISubject


class AppButton(toga.Button):
    """General styled application button."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the button."""
        super().__init__(*args, **kwargs)
        self.style.flex = 1
        self.style.height = BUTTON_HEIGHT
        self.style.font_size = FONT_SIZE_APP


class _ButtonHandler:
    """Base button event handler (internal implementation).

    Should not be used directly - use specific handler classes instead.
    """

    def __init__(self, subject: ISubject) -> None:
        """Construct the handler."""
        self._subject = subject

    def add_listener(self, listener: object) -> None:
        """Register an event listener."""
        return self._subject.add_listener(listener)


class PressButtonMixin:
    """Mixin providing button press event handling."""

    _subject: ISubject

    def handle_button_press(self, button: toga.Button) -> None:
        """Handle button press and notify observers."""
        self._subject.notify('handle_button_press', value=button.text)


class NavigateButtonMixin:
    """Mixin providing navigation event handling."""

    _subject: ISubject

    def navigate(self, button: toga.Button) -> None:
        """Handle navigation event and notify observers."""
        self._subject.notify('navigate', nav_id=button.text)


class NavigateButtonHandler(NavigateButtonMixin, _ButtonHandler):
    """Handler for navigation button events."""


class PressButtonHandler(PressButtonMixin, _ButtonHandler):
    """Handler for press button events."""


class ComboButtonHandler(
    PressButtonHandler,
    NavigateButtonMixin,
    _ButtonHandler,
):
    """Combined handler supporting both press and navigation events.

     Inherits:
        - PressButtonHandler: Handle clicks
        - NavigateButtonMixin: Handling navigation
    """
