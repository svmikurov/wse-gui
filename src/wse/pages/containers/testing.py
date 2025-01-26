"""Foreign word test exercise."""

import toga
from toga.constants import COLUMN
from toga.style import Pack

from wse import constants as const
from wse.controllers.testing import ControllerTest
from wse.pages.handlers.goto_handler import goto_back_handler
from wse.pages.widgets.box import BoxFlexCol
from wse.pages.widgets.box_page import BaseBox
from wse.pages.widgets.button import BtnApp
from wse.pages.widgets.choice import ChoiceBox
from wse.pages.widgets.label import TitleLabel


class TestWidgets:
    """Foreign word test exercise widgets."""

    url_question: str

    def __init__(self, controller: ControllerTest) -> None:
        """Construct the page."""
        super().__init__()
        self._plc = controller
        self._plc.add_listener(self)
        self._plc.url_question = self.url_question
        # Choice boxes are dynamically created
        # based on the number of answer options.
        self._choicebox_name = '_choicebox_%s'

        _style_label = Pack(padding=(0, 0, 0, 7))

        # fmt: off
        self._label_title = TitleLabel(const.TITLE_FOREIGN_TEST)
        self._label_question = toga.Label('Вопрос:', style=_style_label)
        self._label_result = toga.Label('Правильный ответ:', style=_style_label)  # noqa: E501
        self._label_answer = toga.Label('Ответ:', style=_style_label)

        self._text_panel_question = toga.MultilineTextInput(
            style=Pack(flex=1, height=46, font_size=14),
        )

        self._btn_submit = BtnApp('Ответить', on_press=self._plc.submit_handler)  # noqa: E501
        self._btn_next_question = BtnApp('Далее', on_press=self._plc.next_handler)  # noqa: E501
        self._btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)
        # fmt: on

    async def on_open(self, widget: toga.Widget) -> None:
        """Invoke methods on page open."""
        await self._plc.on_open(widget)

    #####################################################################
    # Notifications

    def populate_question(self, question: str) -> None:
        """Populate the question text panel."""
        self._text_panel_question.value = question

    def create_choices(self, choices: tuple[tuple[str, str], ...]) -> None:
        """Create a checkboxes."""
        for index, _ in choices:
            source = self._plc.create_source(index)
            choicebox = ChoiceBox(
                style=Pack(padding=(7, 0, 7, 0)),
                style_switch=Pack(padding=(0, 5, 0, 5)),
                style_text=Pack(height=46, font_size=14, padding_left=15),
                on_change=source.update_value,
            )
            setattr(self, self._choicebox_name % index, choicebox)

    def populate_choices(
        self, choices: tuple[tuple[str, str], ...]
    ) -> None:
        for index, value in choices:
            choicebox = getattr(self, self._choicebox_name % index)
            choicebox.change(value)


class TestLayout(TestWidgets, BaseBox):
    """Foreign word test layout."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the page."""
        super().__init__(*args, **kwargs)
        self._box_test = toga.Box(style=Pack(direction=COLUMN))
        self._box_checkboxes = toga.Box(style=Pack(direction=COLUMN))
        self._box_result = toga.Box(style=Pack(direction=COLUMN))
        self._box_alignment = BoxFlexCol()

        # DOM
        self.add(
            self._label_title,
            self._box_test,
            self._box_alignment,
            self._btn_submit,
            self._btn_goto_back,
        )
        self._box_test.add(
            self._label_question,
            self._text_panel_question,
            self._label_answer,
        )

    #####################################################################
    # Notifications

    def add_choices(self, choices: tuple[tuple[str, str], ...]) -> None:
        """Add choices to page."""
        for index, _ in choices:
            checkbox: ChoiceBox = getattr(self, self._choicebox_name % index)
            self._box_checkboxes.add(checkbox)
        self._box_test.add(self._box_checkboxes)

    def remove_choices(self) -> None:
        """Remove task choices from page."""
        self._box_checkboxes.clear()

    def display_result_widgets(self) -> None:
        """Display answer result widgets."""
        self.replace(self._box_test, self._box_result)
        self.replace(self._btn_submit, self._btn_next_question)

    def display_test_widgets(self) -> None:
        """Display widgets for test question."""
        self.replace(self._box_result, self._box_test)
        self.replace(self._btn_next_question, self._btn_submit)
