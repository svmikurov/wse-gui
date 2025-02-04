"""Custom number keyboard container."""

import toga
from toga.constants import COLUMN
from toga.sources import Listener, Source

from wse.pages.widgets.box import BoxFlexRow

BUTTON_HEIGHT = 70
FONT_SIZE = 20
MAX_DIGIT_COUNT = 19


class KeyboardButton(toga.Button):
    """Number keyboard button."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the button."""
        super().__init__(*args, **kwargs)
        self.style.flex = 1
        self.style.height = BUTTON_HEIGHT
        self.style.font_size = FONT_SIZE


class NumKeyboardController(Source):
    """Number keyboard controller."""

    def __init__(self) -> None:
        """Construct the controller."""
        super().__init__()
        self.number: str = ''
        self.max_digit_count = MAX_DIGIT_COUNT

    def num_handler(self, widget: toga.Button) -> None:
        """Handle press a number button."""
        if len(self.number) < self.max_digit_count:
            symbol = widget.text
            self.number += symbol
            self._update_num_panel()

    def point_handler(self, widget: toga.Button) -> None:
        """Handle press a point button."""
        symbol = widget.text
        if (
            symbol not in self.number
            and len(self.number) < self.max_digit_count - 1
        ):
            self.number += symbol
            self._update_num_panel()

    def backspace_handler(self, _: toga.Button) -> None:
        """Handle press the backspace."""
        self.number = self.number[: len(self.number) - 1]
        self._update_num_panel()

    def clean(self) -> None:
        """Clean entered text."""
        self.number = ''
        self._update_num_panel()

    ####################################################################
    # Notifications

    def _update_num_panel(self) -> None:
        self.notify('update_num_panel', text=self.number)


class NumKeyboard(toga.Box):
    """Custom number keyboard container."""

    def __init__(self, max_digit_count: int | None = None) -> None:
        """Construct the container."""
        super().__init__()
        self.style.direction = COLUMN
        self.plc = NumKeyboardController()
        if max_digit_count:
            self.plc.max_digit_count = max_digit_count

        _btn_0 = KeyboardButton(text='0', on_press=self.plc.num_handler)
        _btn_1 = KeyboardButton(text='1', on_press=self.plc.num_handler)
        _btn_2 = KeyboardButton(text='2', on_press=self.plc.num_handler)
        _btn_3 = KeyboardButton(text='3', on_press=self.plc.num_handler)
        _btn_4 = KeyboardButton(text='4', on_press=self.plc.num_handler)
        _btn_5 = KeyboardButton(text='5', on_press=self.plc.num_handler)
        _btn_6 = KeyboardButton(text='6', on_press=self.plc.num_handler)
        _btn_7 = KeyboardButton(text='7', on_press=self.plc.num_handler)
        _btn_8 = KeyboardButton(text='8', on_press=self.plc.num_handler)
        _btn_9 = KeyboardButton(text='9', on_press=self.plc.num_handler)
        _btn_point = KeyboardButton(text='.', on_press=self.plc.point_handler)
        _btn_backspace = KeyboardButton(
            text='<-', on_press=self.plc.backspace_handler
        )

        # DOM
        self.add(
            BoxFlexRow(children=[_btn_1, _btn_2, _btn_3]),
            BoxFlexRow(children=[_btn_4, _btn_5, _btn_6]),
            BoxFlexRow(children=[_btn_7, _btn_8, _btn_9]),
            BoxFlexRow(children=[_btn_point, _btn_0, _btn_backspace]),
        )

    def add_listener(self, listener: Listener) -> None:
        """Add a new listener."""
        self.plc.add_listener(listener)

    def clean(self) -> None:
        """Clean the entered digits."""
        self.plc.clean()
