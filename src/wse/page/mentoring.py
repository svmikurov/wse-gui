"""Mentoring page."""

from urllib.parse import urljoin

from toga.style import Pack

from wse.constants import FOREIGN_TESTING_PATH, HOST
from wse.page.containers.testing import TestLayout
from wse.page.handlers.goto_handler import (
    goto_back_handler,
    goto_word_test_handler,
)
from wse.page.widgets.box_page import BaseBox
from wse.page.widgets.button import BtnApp
from wse.page.widgets.label import TitleLabel
from wse.page.widgets.text_input import InfoTextPanel


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

    url_question = urljoin(HOST, FOREIGN_TESTING_PATH)
    url_answer = urljoin(HOST, FOREIGN_TESTING_PATH)
