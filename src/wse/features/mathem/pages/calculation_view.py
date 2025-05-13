"""Defines the View for the Multiplication Exercise page."""

from dataclasses import dataclass
from typing import Any

import toga
from toga.style import Pack

from wse.core.i18n import _
from wse.core.navigation.navigation_id import NavID
from wse.features.base.mvc_ import BaseView
from wse.features.mathem.interfaces.ipages import ICalculationView
from wse.features.shared.enums import ObjectID, StyleID, TaskState
from wse.interface.iobserver import IStateSubject
from wse.interface.iui.ikeypad import IKeypad


@dataclass
class CalculationView(BaseView, ICalculationView):
    """Multiplication page view."""

    display_question: IStateSubject
    display_answer: IStateSubject
    display_info: IStateSubject
    keypad: IKeypad

    def __post_init__(self) -> None:
        """Post init."""
        super().__post_init__()
        self._content.id = ObjectID.MULTIPLICATION

    def _populate_content(self) -> None:
        self._content.add(
            self._title_label,
            self._question_label,
            self.display_question.content,
            self._answer_label,
            self.display_answer.content,
            self._info_label,
            self.display_info.content,
            toga.Box(style=Pack(flex=1)),  # Flex stub
            self.keypad.content,
            self._answer_button,
            self._back_button,
        )

    def _create_ui(self) -> None:
        self._title_label = toga.Label(text='')
        self._question_label = toga.Label(text='')
        self._answer_label = toga.Label(text='')
        self._info_label = toga.Label(text='')
        self._answer_button = self._create_button()
        self._back_button = self._create_nav_btn()

    # Localize widget text

    def localize_ui(self) -> None:
        """Localize a text for user interface widgets."""
        self._title_label.text = _('Multiplication title')
        self._question_label.text = _('Question')
        self._answer_label.text = _('Answer input')
        self._info_label.text = _('Result info')
        self._answer_button.text = _(TaskState.ANSWER_CHECKING)
        self._back_button.text = _(NavID.BACK)

    # Widget style

    @property
    def _ui_styles(self) -> dict[Any, StyleID]:
        return {
            self._title_label: StyleID.TITLE,
            self._question_label: StyleID.DEFAULT_LABEL,
            self.display_question: StyleID.LINE_DISPLAY,
            self._answer_label: StyleID.DEFAULT_LABEL,
            self.display_answer: StyleID.LINE_DISPLAY,
            self._info_label: StyleID.DEFAULT_LABEL,
            self.display_info: StyleID.RESULT_INFO_DISPLAY,
            self._answer_button: StyleID.DEFAULT_BUTTON,
            self._back_button: StyleID.DEFAULT_BUTTON,
        }

    # Utility methods

    def _create_button(self) -> toga.Button:
        return toga.Button(on_press=self.button_handler.button_press)  # type: ignore
