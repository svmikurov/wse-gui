"""Multiplication exercise page."""

import toga
from toga.constants import LEFT, RIGHT

from wse.controllers.multiplication import MultiplicationController
from wse.pages.containers.num_keyboard import NumKeyboard
from wse.pages.handlers.goto_handler import goto_back_handler
from wse.pages.widgets.box import BoxFlexCol
from wse.pages.widgets.box_page import BaseBox
from wse.pages.widgets.button import BtnApp
from wse.pages.widgets.label import TitleLabel
from wse.pages.widgets.text_input import ListenerMixin

NUM_FONT_SIZE = 48
HEIGHT_VS_FONT_SIZE_RATIO = 1.6
MAX_DIGIT_COUNT = 3
NUM_HEIGHT = int(NUM_FONT_SIZE * HEIGHT_VS_FONT_SIZE_RATIO)


class NumInput(ListenerMixin, toga.MultilineTextInput):
    """Number input panel."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the widget."""
        super().__init__(*args, **kwargs)
        self.readonly = True
        self.placeholder = '0.0'
        self.style.flex = 1
        self.style.height = NUM_HEIGHT
        self.style.text_align = RIGHT
        self.style.font_size = NUM_FONT_SIZE


class MultiplicationWidgets:
    """Multiplication exercise widgets."""

    title: str

    def __init__(self, controller: MultiplicationController) -> None:
        """Construct the page."""
        super().__init__()
        self._plc = controller

        # fmt: off
        self._label_title = TitleLabel(text=self.title)
        self._label_question = toga.Label(text='Вопрос:')
        self._label_answer = toga.Label(text='Ответ:')

        self._text_question = NumInput()
        self._text_question.value = '2 x 4 = '
        self._text_question.style.flex = 2

        self._input_answer = NumInput()
        self._input_answer.placeholder = '?'
        self._input_answer.style.flex = 1
        self._input_answer.style.text_align = LEFT

        self._num_keyboard = NumKeyboard(max_digit_count=MAX_DIGIT_COUNT)
        self._num_keyboard.plc.add_listener(self)

        self._btn_submit = BtnApp('Ответить', on_press=self._plc.submit_handler)  # noqa: E501
        self._btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)
        # fmt: on

    async def on_open(self, widget: toga.Widget) -> None:
        """Invoke methods on page open."""
        await self._plc.on_open(widget)

    ####################################################################
    # Listener methods

    def change(self, text: str) -> None:
        """Change the answer numbers."""
        self._input_answer.value = text


class MultiplicationLayout(MultiplicationWidgets, BaseBox):
    """Multiplication exercise layout."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the layout."""
        super().__init__(*args, **kwargs)

        _box_task = toga.Box()
        _box_align = BoxFlexCol()
        _box_btns = toga.Box()

        # DOM
        self.add(
            self._label_title,
            _box_task,
            _box_align,
            self._num_keyboard,
            _box_btns,
        )
        _box_task.add(
            self._text_question,
            self._input_answer,
        )
        _box_btns.add(self._btn_goto_back, self._btn_submit)
