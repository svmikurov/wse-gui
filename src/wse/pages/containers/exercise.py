"""Exercise."""

from typing import TypeVar

import toga
from toga import MultilineTextInput
from toga.style.pack import Pack

from wse.pages.widgets.box_page import BaseBox
from wse.pages.widgets.button import AnswerBtn
from wse.pages.widgets.label import TitleLabel
from wse.pages.widgets.text_input import TextPanel

T = TypeVar('T')


class ExerciseWidgets:
    """Exercise widgets."""

    title = ''

    def __init__(self, controller: T) -> None:
        """Construct a exercise widgets."""
        super().__init__()
        self.plc = controller

        # fmt: off
        # Style
        label_style = Pack(padding=(0, 0, 0, 7))

        # Title
        self.label_title = TitleLabel(self.title)

        # Labels
        self.label_question = toga.Label('Вопрос:', style=label_style)
        self.label_answer = toga.Label('Ответ:', style=label_style)

        # Task text display widgets
        self.text_panel_question = TextPanel(style=Pack(flex=2))
        self.text_panel_answer = TextPanel(style=Pack(flex=2))

        # Task info display widgets
        self.label_text_panel = toga.Label('Информация об упражнении:')
        self.label_text_panel.style = Pack(padding=(0, 0, 0, 7))
        self.text_panel_info = MultilineTextInput(style=Pack(flex=1), readonly=True)  # noqa: E501

        # Exercise buttons
        self.btn_pause = AnswerBtn('Пауза', on_press=self.plc.pause)
        self.btn_not_know = AnswerBtn('Не знаю', on_press=self.plc.not_know)
        self.btn_know = AnswerBtn('Знаю', on_press=self.plc.know)
        self.btn_next = AnswerBtn('Далее', on_press=self.plc.next)

        # Listeners
        self.plc.question.add_listener(self.text_panel_question)
        self.plc.answer.add_listener(self.text_panel_answer)
        self.plc.info.add_listener(self.text_panel_info)
        # fmt: on

    async def on_open(self, _: toga.Widget) -> None:
        """Start exercise when box was assigned to window content."""
        await self.plc.start()


class ExerciseLayout(ExerciseWidgets, BaseBox):
    """Layout of exercise box-container."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the box."""
        super().__init__(*args, **kwargs)

        # Exercise buttons are enclosed in box.
        self.box_btns = toga.Box(style=Pack(height=100))

        # DOM.
        self.add(
            self.label_question,
            self.text_panel_question,
            self.label_answer,
            self.text_panel_answer,
            self.label_text_panel,
            self.text_panel_info,
            self.box_btns,
        )
        self.box_btns.add(
            self.btn_pause,
            self.btn_not_know,
            self.btn_know,
            self.btn_next,
        )
