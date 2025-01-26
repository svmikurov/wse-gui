"""Mentoring page."""

from toga.style import Pack

from wse.pages.containers.testing import TestLayout
from wse.pages.handlers.goto_handler import (
    goto_back_handler,
    goto_word_test_handler,
)
from wse.pages.widgets.box_page import BaseBox
from wse.pages.widgets.button import BtnApp
from wse.pages.widgets.label import TitleLabel
from wse.pages.widgets.text_input import InfoTextPanel


class MentoringPage(BaseBox):
    """Mentoring page."""

    _info = ''

    def __init__(self) -> None:
        """Construct the page."""
        super().__init__()

        self._label_title = TitleLabel('Задания')

        # Info panel
        self._info_panel = InfoTextPanel(style=Pack(flex=1), value=self._info)

        # Buttons
        self._btn_goto_test = BtnApp(
            'Тест по иностранному языку', on_press=goto_word_test_handler
        )
        self._btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)

        # DOM
        self.add(
            self._info_panel,
            self._btn_goto_test,
            self._btn_goto_back,
        )


class WordTestPage(TestLayout):
    """A vocabulary test page."""

    url_question = 'http://127.0.0.1/api/v1/foreign/assigned/test/'
