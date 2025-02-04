"""Foreign word test exercise."""

from typing import TypeVar

import toga
from toga.constants import COLUMN
from toga.sources import Source
from toga.style import Pack

from wse import constants as const
from wse.controllers.testing import ControllerTest
from wse.pages.handlers.goto_handler import goto_back_handler
from wse.pages.widgets.box import BoxFlexCol
from wse.pages.widgets.box_page import BaseBox
from wse.pages.widgets.button import BtnApp
from wse.pages.widgets.choice import ChoiceBox
from wse.pages.widgets.label import TitleLabel

SourceT = TypeVar('SourceT', bound=Source)

CHOICE_TEXT_HEIGHT = 48
CHOICE_TEXT_SIZE = 14
SWITCH_WIDTH = 70


class TestWidgets:
    """Foreign word test exercise widgets."""

    url_question: str
    url_answer: str

    def __init__(self, controller: ControllerTest) -> None:
        """Construct the pages."""
        super().__init__()
        self._plc = controller
        self._plc.add_listener(self)
        self._plc.url_question = self.url_question
        self._plc.url_answer = self.url_answer
        # Choice boxes are dynamically created
        # based on the number of answer options.
        self._choice_box_name = '_choice_box_%s'

        _style_label = Pack(padding=(0, 0, 0, 7))

        # fmt: off
        self._label_title = TitleLabel(const.TITLE_FOREIGN_TEST)
        self._label_question = toga.Label('Вопрос:', style=_style_label)
        self._label_result = toga.Label('Правильный ответ:', style=_style_label)  # noqa: E501
        self._label_answer = toga.Label('Ответ:', style=_style_label)

        self._text_panel_question = toga.MultilineTextInput(
            style=Pack(
                flex=1,
                height=CHOICE_TEXT_HEIGHT * const.PHONE_SCALING,
                font_size=CHOICE_TEXT_SIZE,
            ),
        )

        self._btn_submit = BtnApp('Ответить', on_press=self._plc.submit_handler)  # noqa: E501
        self._btn_next_question = BtnApp('Далее', on_press=self._plc.next_handler)  # noqa: E501
        self._btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)
        # fmt: on

    async def on_open(self, widget: toga.Widget) -> None:
        """Invoke methods on pages open."""
        await self._plc.on_open(widget)

    #####################################################################
    # Notifications

    def populate_question(self, question: str) -> None:
        """Populate the question text panel."""
        self._text_panel_question.value = question

    def clear_question(self) -> None:
        """Clear a question field."""
        self._text_panel_question.value = ''

    def add_choice(self, index: int, source: SourceT) -> None:
        """Create a choice box."""
        choice_box = ChoiceBox(
            style_switch=Pack(
                width=SWITCH_WIDTH,
            ),
            style_text=Pack(
                height=CHOICE_TEXT_HEIGHT * const.PHONE_SCALING,
                font_size=CHOICE_TEXT_SIZE,
            ),
            on_change=source.update_value,
        )
        setattr(self, self._choice_box_name % index, choice_box)
        source.add_listener(choice_box)
        self._display_choice_box(choice_box)

    def _display_choice_box(self, choice_box: ChoiceBox) -> None:
        raise NotImplementedError(
            '`_display_choice_box()` must be implemented.'
        )


class TestLayout(TestWidgets, BaseBox):
    """Foreign word test layout."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the pages."""
        super().__init__(*args, **kwargs)
        self._box_test = BoxFlexCol()
        self._box_checkboxes = BoxFlexCol()
        self._box_result = toga.Box(style=Pack(direction=COLUMN))

        # Check boxes are included in scroll container.
        self._scroll_checkboxes = toga.ScrollContainer(
            style=Pack(flex=1, direction=COLUMN),
            content=self._box_checkboxes,
        )

        # DOM
        self.add(
            self._label_title,
            self._box_test,
            self._btn_submit,
            self._btn_goto_back,
        )
        self._box_test.add(
            self._label_question,
            self._text_panel_question,
            self._label_answer,
            self._scroll_checkboxes,
        )

    #####################################################################
    # Notifications

    def _display_choice_box(self, choice_box: ChoiceBox) -> None:
        self._box_checkboxes.add(choice_box)

    def remove_choices(self) -> None:
        """Remove task choices from pages."""
        self._box_checkboxes.clear()

    def display_result_widgets(self) -> None:
        """Display answer result widgets."""
        self.replace(self._box_test, self._box_result)
        self.replace(self._btn_submit, self._btn_next_question)

    def display_test_widgets(self) -> None:
        """Display widgets for test question."""
        self.replace(self._box_result, self._box_test)
        self.replace(self._btn_next_question, self._btn_submit)
