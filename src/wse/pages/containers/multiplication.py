"""Multiplication exercise pages."""

from typing import TypeVar

import toga
from toga.constants import LEFT, RIGHT
from toga.sources import Listener
from toga.style import Pack

from wse.pages.base import BasePage
from wse.pages.containers.num_keyboard import NumKeyboard
from wse.pages.handlers.goto_handler import goto_back_handler
from wse.pages.widgets.box import BoxFlexCol, BoxFlexRow
from wse.pages.widgets.button import BtnApp

NUM_FONT_SIZE = 48
HEIGHT_VS_FONT_SIZE_RATIO = 1.6
MAX_DIGIT_COUNT = 3
NUM_HEIGHT = int(NUM_FONT_SIZE * HEIGHT_VS_FONT_SIZE_RATIO)

ContrT = TypeVar('ContrT', bound=Listener)


class Panel(toga.Label):
    """One line panel widget."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the widget."""
        kwargs['text'] = kwargs.setdefault('text', '')
        super().__init__(*args, **kwargs)
        self.style.height = NUM_HEIGHT
        self.style.font_size = NUM_FONT_SIZE


class MultiplicationWidgets(BasePage):
    """Multiplication exercise widgets."""

    _padding = (30, 0, 0, 0)

    def __init__(self) -> None:
        """Construct the pages."""
        super().__init__()

        # Panels
        self.question_text = Panel(style=Pack(flex=2, text_align=RIGHT))
        self.input_answer = Panel(style=Pack(flex=1, text_align=LEFT))
        self.panel_result = Panel(style=Pack(padding=self._padding))

        # Buttons
        self.num_keyboard = NumKeyboard(max_digit_count=MAX_DIGIT_COUNT)
        self.btn_submit = BtnApp('Ответить')
        _btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)

        # Inner boxes
        _box_task = toga.Box(
            style=Pack(padding=self._padding),
            children=[self.question_text, self.input_answer],
        )
        _box_align = BoxFlexCol()
        _box_btns = toga.Box(children=[_btn_goto_back, self.btn_submit])

        # Outer boxes
        _box_task_outer = toga.Box(
            children=[BoxFlexRow(), _box_task, BoxFlexRow()]
        )
        _box_panel_result_outer = toga.Box(
            children=[BoxFlexRow(), self.panel_result, BoxFlexRow()]
        )

        # DOM
        self.add(
            _box_task_outer,
            _box_panel_result_outer,
            _box_align,
            self.num_keyboard,
            _box_btns,
        )
