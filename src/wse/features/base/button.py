"""Defines base classes for mathematical."""

from abc import ABC, abstractmethod

import toga

from wse.interface.ifeatures import IContent
from wse.interface.iui.ibutton import IButtonFactory, IButtonHandler


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


class BaseKeypadBuilder(ABC):
    """Base button box."""

    def __init__(
        self,
        handler: IButtonHandler,
        content: IContent,
        button_factory: IButtonFactory,
    ) -> None:
        """Construct the box."""
        self._handler = handler
        self._content = content
        self._button_factory = button_factory

        # Build box
        self._build_button_line()
        self._build_buttons()
        self._build_keypad()

    # Keypad building

    @property
    def content(self) -> IContent:
        """Widget box content."""
        return self._content

    @abstractmethod
    def _build_keypad(self) -> None:
        """Add buttons to keypad content."""

    @abstractmethod
    def _build_button_line(self) -> None:
        """Build a line of buttons."""

    @abstractmethod
    def _build_buttons(self) -> None:
        """Build a buttons."""

    # Button creation

    def _create_button(
        self, symbol: int | str, **kwargs: object
    ) -> toga.Button:
        """Create a button."""
        return self._button_factory.create_button(
            symbol,
            on_press=self._handler.handle_button_press,
            **kwargs,
        )

    def subscribe(self, listener: object) -> None:
        """Register an observer to receive notifications."""
        self._handler.subject.add_listener(listener=listener)
