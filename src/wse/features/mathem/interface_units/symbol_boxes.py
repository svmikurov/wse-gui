"""Defines symbol boxes fo numeric keyboard."""

import toga
from toga.style import Pack
from typing_extensions import override

from wse.features.mathem.interface_units.base import BaseButtonBox, ButtonLine


class DigitButtonBox(BaseButtonBox):
    """Digit buttons box."""

    _KWARGS = {'style': Pack(font_weight='bold')}

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the box."""
        super().__init__(*args, **kwargs)
        self._style_button()

    def _fill_content(self) -> None:
        self._content.add(
            self._buttons_line_1,
            self._buttons_line_2,
            self._buttons_line_3,
            self._buttons_line_4,
        )

        self._buttons_line_1.add(self._btn_1, self._btn_2, self._btn_3)
        self._buttons_line_2.add(self._btn_4, self._btn_5, self._btn_6)
        self._buttons_line_3.add(self._btn_7, self._btn_8, self._btn_9)
        self._buttons_line_4.add(self._btn_d, self._btn_0, self._btn_e)

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
        self._btn_e = self._create_button('=')  # equal sign

    def _style_button(self) -> None:
        self._btn_5.style.color = 'green'

    @override
    def _create_button(
        self, symbol: int | str, **kwargs: object
    ) -> toga.Button:
        """Create a button with additional style."""
        return super()._create_button(symbol, **self._KWARGS)


class ActionButtonBox(BaseButtonBox):
    """Numbers box."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the box."""
        super().__init__(*args, **kwargs)

    def _fill_content(self) -> None:
        self._content.add(self._buttons_line)

        self._buttons_line.add(
            self._btn_delete,
            self._btn_cancel,
            self._btn_enter,
        )

    def _build_button_line(self) -> None:
        self._buttons_line = ButtonLine(style=Pack(direction='column'))

    def _build_buttons(self) -> None:
        self._btn_delete = self._create_button('del')
        self._btn_cancel = self._create_button('C')
        self._btn_enter = self._create_button('↵')


class SignButtonBox(BaseButtonBox):
    """Box with sign buttons."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the box."""
        super().__init__(*args, **kwargs)

    def _fill_content(self) -> None:
        self._content.add(self._buttons_line)

        self._buttons_line.add(
            self._btn_add,
            self._btn_sub,
            self._btn_mul,
            self._btn_div,
        )

    def _build_button_line(self) -> None:
        """Build button line."""
        self._buttons_line = ButtonLine(style=Pack(direction='column'))

    def _build_buttons(self) -> None:
        """Build sign buttons."""
        self._btn_add = self._create_button('+')
        self._btn_sub = self._create_button('-')
        self._btn_mul = self._create_button('x')
        self._btn_div = self._create_button('/')
