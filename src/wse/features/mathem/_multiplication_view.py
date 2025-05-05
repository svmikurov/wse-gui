"""Defines Multiplication page view."""

import toga
from toga.style import Pack

from wse.core.i18n import _
from wse.core.navigation.navigation_id import NavID
from wse.features.base.mvc import BaseView
from wse.features.shared.boxes import ColumnFlexBox
from wse.features.shared.enums.object_id import ObjectID
from wse.features.shared.ui.button import AppButton
from wse.features.shared.ui.ui_text import TextInLinePanel, TitleLabel
from wse.interface.iui.ikeypad import IKeypad


class _MultiplicationView(BaseView):
    """Multiplication page view."""

    def __init__(
        self,
        *args: object,
        keypad: IKeypad,
        **kwargs: object,
    ) -> None:
        """Construct the view."""
        super().__init__(*args, **kwargs)
        self.keypad = keypad
        self._content.id = ObjectID.MULTIPLICATION

        self._flex_box = ColumnFlexBox()
        self._add_ui()

    def _add_ui(self) -> None:
        self.content.add(
            self._label_title,
            # Question UI
            self._label_question,
            self.text_inline_panel,
            # Answer UI
            self._label_answer,
            self.input_text,
            # Control UI
            self._flex_box,
            self.keypad.content,
            self._btn_check_answer,
            self._btn_back,
        )

    def _create_ui(self) -> None:
        """Build a user interface."""
        self._label_title = TitleLabel()

        # Question UI
        self._label_question = toga.Label(text='')
        self.text_inline_panel = TextInLinePanel(
            style=Pack(
                padding=(7, 2, 7, 2),
                text_align='center',
                font_size=24,
            )
        )

        # Answer UI
        self._label_answer = toga.Label(text='')
        self.input_text = TextInLinePanel(
            style=Pack(
                padding=(7, 2, 7, 2),
                font_size=24,
            )
        )

        # Control UI
        self._btn_check_answer = AppButton(on_press=self._handel_answer)
        self._btn_back = self._build_nav_btn()

    def localize_ui(self) -> None:
        """Localize a text for user interface widgets."""
        self._label_title.text = _('Multiplication title')
        self._label_question.text = _('Question')
        self._label_answer.text = _('Answer input')
        self._btn_check_answer.text = _('Check answer')
        self._btn_back.text = _(NavID.BACK)

    def _handel_answer(self, _: toga.Button) -> None:
        """Handel task answer."""
        answer = '5'
        self.subject.notify('check_answer', value=answer)
