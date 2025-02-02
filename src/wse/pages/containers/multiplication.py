"""Multiplication exercise page."""

import toga
from toga.constants import LEFT, RIGHT
from toga.style import Pack

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
        self.style.height = NUM_HEIGHT
        self.style.font_size = NUM_FONT_SIZE


class MultiplicationWidgets:
    """Multiplication exercise widgets."""

    title: str

    def __init__(self, controller: MultiplicationController) -> None:
        """Construct the page."""
        super().__init__()
        self._plc = controller

        self._label_title = TitleLabel(text=self.title)

        self._question = NumInput()

        self._answer = NumInput()
        self._answer.placeholder = '?'
        self._answer.on_change = self._plc.update_value

        self._result = toga.MultilineTextInput(readonly=True)

        self._num_keyboard = NumKeyboard(max_digit_count=MAX_DIGIT_COUNT)

        # This widget is a listener.
        self._plc.add_listener(self)
        self._num_keyboard.plc.add_listener(self)

        self._btn_submit = BtnApp(
            'Ответить',
            on_press=self._plc.submit_handler,
        )
        self._btn_goto_back = BtnApp(
            'Назад',
            on_press=goto_back_handler,
        )

    async def on_open(self, widget: toga.Widget) -> None:
        """Invoke methods on page open."""
        await self._plc.on_open(widget)

    ####################################################################
    # Listener methods

    def display_answer(self, text: str) -> None:
        """Change the answer numbers."""
        self._answer.value = text

    def clear_answer(self) -> None:
        """Clear text of answer."""
        self._num_keyboard.plc.clear()

    def display_question(self, text: str) -> None:
        """Display the task question."""
        question = f'{text} = '
        self._question.value = question

    def clear_question(self) -> None:
        """Clear text of question."""
        self._question.value = ''

    def display_result(self, text: str) -> None:
        """Display answer result."""
        self._result.value = text
        self.clear_answer()

    def clear_result(self) -> None:
        """Clear text of result."""
        self._result.value = None


class MultiplicationLayout(MultiplicationWidgets, BaseBox):
    """Multiplication exercise layout."""

    _task_padding = (20, 0, 0, 0)
    _result_padding = (20, 0, 0, 0)

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the layout."""
        super().__init__(*args, **kwargs)

        self._question.style.flex = 2
        self._question.style.text_align = RIGHT

        self._answer.style.flex = 1
        self._answer.style.text_align = LEFT

        self._result.style.flex = 1
        self._result.style.font_size = 32
        self._result.style.padding = self._result_padding

        _box_task = toga.Box(
            style=Pack(padding=self._task_padding),
            children=[self._question, self._answer],
        )
        _box_align = BoxFlexCol()
        _box_btns = toga.Box(children=[self._btn_goto_back, self._btn_submit])

        # DOM
        self.add(
            self._label_title,
            _box_task,
            self._result,
            _box_align,
            self._num_keyboard,
            _box_btns,
        )
