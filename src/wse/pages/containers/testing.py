"""Foreign word test exercise."""

import toga
from toga.constants import COLUMN
from toga.style import Pack

from wse import constants as const
from wse.pages.handlers.goto_handler import goto_back_handler
from wse.pages.widgets.box import BoxFlexCol
from wse.pages.widgets.box_page import BaseBox
from wse.pages.widgets.button import BtnApp
from wse.pages.widgets.label import TitleLabel
from wse.pages.widgets.switch import SwitchApp

TASK = {
    'question': 'question',
    'answer': (
        ('1', 'answer var 1'),
        ('2', 'answer answer answer answer answer answer var 2'),
        ('3', 'answer var 3'),
        ('4', 'answer var 4'),
        ('5', 'answer var 5'),
        ('6', 'answer var 6'),
        ('7', 'answer var 7'),
    ),
}


class TestWidgets:
    """Foreign word test exercise widgets."""

    def __init__(self) -> None:
        """Construct the page."""
        super().__init__()
        self._answer_checkbox_count = len(TASK['answer'])

        _label_style = Pack(padding=(0, 0, 0, 7))

        self._label_title = TitleLabel(const.TITLE_FOREIGN_TEST)
        self._label_question = toga.Label('Вопрос:', style=_label_style)
        self._label_answer = toga.Label('Ответ:', style=_label_style)

        self._text_panel_question = toga.MultilineTextInput(
            style=Pack(flex=1, height=46, font_size=14),
            value=TASK['question'],
        )

        self._btn_submit_answer = BtnApp('Ответить', on_press=...)
        self._btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)

        self._create_answer_checkboxes()

    def _create_answer_checkboxes(self) -> None:
        for index, text in TASK['answer']:
            box = toga.Box(
                style=Pack(padding=(7, 0, 7, 0)),
                children=[
                    toga.Box(
                        style=Pack(direction=COLUMN, padding=(0, 5, 0, 5)),
                        children=[SwitchApp(text='')],
                    ),
                    toga.MultilineTextInput(
                        style=Pack(
                            flex=1,
                            height=46,
                            font_size=14,
                            padding=(0, 0, 0, 15),
                        ),
                        readonly=True,
                        value=text,
                    ),
                ],
            )
            setattr(self, f'_checkbox_{index}', box)


class TestLayout(TestWidgets, BaseBox):
    """Foreign word test layout."""

    def __init__(self) -> None:
        """Construct the page."""
        super().__init__()
        self._box_test = toga.Box(style=Pack(direction=COLUMN))
        self._box_alignment = BoxFlexCol()

        # DOM
        self.add(
            self._label_title,
            self._box_test,
            self._box_alignment,
            self._btn_submit_answer,
            self._btn_goto_back,
        )
        self._box_test.add(
            self._label_question,
            self._text_panel_question,
            self._label_answer,
        )
        self._add_checkboxes()

    def _add_checkboxes(self) -> None:
        """Add checkbox to box."""
        for index, _ in TASK['answer']:
            checkbox: SwitchApp = getattr(self, f'_checkbox_{index}')
            self._box_test.add(checkbox)
