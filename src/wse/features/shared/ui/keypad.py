"""Defines symbol boxes fo numeric keyboard."""

import toga
from toga.style import Pack
from typing_extensions import override

from wse.features.base.button import (
    BaseKeypadBuilder,
    ButtonLine,
)


class DigitKeypad(BaseKeypadBuilder):
    """Digit keypad."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the box."""
        super().__init__(*args, **kwargs)
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
        self._buttons_line_1 = ButtonLine()
        self._buttons_line_2 = ButtonLine()
        self._buttons_line_3 = ButtonLine()
        self._buttons_line_4 = ButtonLine()

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

    @override
    def _create_button(
        self, symbol: int | str, **kwargs: object
    ) -> toga.Button:
        """Create a button with additional style."""
        return super()._create_button(symbol)
