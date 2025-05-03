"""Defines symbol boxes fo numeric keyboard."""

import dataclasses

import toga
from toga.style import Pack

from wse.features.shared.enums import StyleID
from wse.interface.ifeatures import IContent
from wse.interface.iui.ibutton import IButtonFactory, IButtonHandler


@dataclasses.dataclass
class DigitKeypad:
    """Digit keypad."""

    _content: IContent
    _button_factory: IButtonFactory
    _button_handler: IButtonHandler
    _style_config: dict

    def __post_init__(self) -> None:
        """Construct the keypad."""
        self._build_button_line()
        self._build_buttons()
        self._build_keypad()
        self._style_button()

    def _build_keypad(self) -> None:
        self._content.add(
            self._buttons_line_1,
            self._buttons_line_2,
            self._buttons_line_3,
            self._buttons_line_4,
        )

        self._buttons_line_1.add(self._btn_1, self._btn_2, self._btn_3)
        self._buttons_line_2.add(self._btn_4, self._btn_5, self._btn_6)
        self._buttons_line_3.add(self._btn_7, self._btn_8, self._btn_9)
        self._buttons_line_4.add(self._btn_d, self._btn_0, self._btn_b)

    def _build_button_line(self) -> None:
        self._buttons_line_1 = toga.Box()
        self._buttons_line_2 = toga.Box()
        self._buttons_line_3 = toga.Box()
        self._buttons_line_4 = toga.Box()

    def _build_buttons(self) -> None:
        self._btn_1 = self._create_button(1)
        self._btn_2 = self._create_button(2)
        self._btn_3 = self._create_button(3)
        self._btn_4 = self._create_button(4)
        self._btn_5 = self._create_button(5)
        self._btn_6 = self._create_button(6)
        self._btn_7 = self._create_button(7)
        self._btn_8 = self._create_button(8)
        self._btn_9 = self._create_button(9)
        self._btn_0 = self._create_button(0)
        self._btn_d = self._create_button('.')  # dote
        self._btn_b = self._create_button('⌫')  # Backspace \u232B

    def _style_button(self) -> None:
        self._btn_5.style.color = 'green'

    # Utility methods

    def _create_button(
        self, symbol: int | str, **kwargs: object
    ) -> toga.Button:
        """Create a button."""
        return self._button_factory.create(
            symbol,
            style=Pack(**self._style_config.get(StyleID.KEYPAD_BUTTON)),
            on_press=self._button_handler.keypad_press,
            **kwargs,
        )

    def subscribe(self, listener: object) -> None:
        """Register an observer to receive notifications."""
        self._button_handler.subject.add_listener(listener=listener)

    @property
    def content(self) -> IContent:
        """Return UI content."""
        return self._content
