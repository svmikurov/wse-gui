"""Defines base classes for mathematical."""

from abc import ABC, abstractmethod
from typing import Callable

import toga

from wse.features.shared.content import SimpleContent
from wse.features.shared.observer import Subject
from wse.interface.ifeatures import IContent, ISubject


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


class ButtonLine(toga.Box):
    """Box of button as line container."""

    _LINE_PADDING = (0, 0, 0, 0)

    def __init__(
        self,
        *args: object,
        padding: tuple = _LINE_PADDING,
        **kwargs: object,
    ) -> None:
        """Construct the button line."""
        super().__init__(*args, **kwargs)
        self.style.padding = padding


class BaseButtonBox(ABC):
    """Base button box."""

    def __init__(
        self,
        subject: ISubject | None = None,
        content: IContent | None = None,
    ) -> None:
        """Construct the box."""
        self._subject = subject if subject is not None else Subject()
        self._content = content if content is not None else SimpleContent()

        # Build box
        self._build_button_line()
        self._build_buttons()
        self._fill_content()

    @abstractmethod
    def _fill_content(self) -> None:
        """Fill content with buttons."""

    @abstractmethod
    def _build_button_line(self) -> None:
        """Build a line of buttons."""

    @abstractmethod
    def _build_buttons(self) -> None:
        """Build a buttons."""

    def _create_button(
        self, symbol: int | str, **kwargs: object
    ) -> toga.Button:
        """Create a button."""
        return KeypadButton(symbol, on_press=self._handle_button, **kwargs)

    def _handle_button(self, button: toga.Button) -> None:
        """Handel the button callback function."""
        self.subject.notify('handle_button', button=button.text)

    @property
    def subject(self) -> ISubject:
        """Subject of Observer pattern."""
        return self._subject

    @property
    def content(self) -> IContent:
        """Widget box content."""
        return self._content
