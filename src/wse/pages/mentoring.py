"""Mentoring pages."""

from urllib.parse import urljoin

from wse.constants import FOREIGN_TESTING_PATH, HOST
from wse.pages.base import BasePage
from wse.pages.containers.testing import TestLayout
from wse.pages.widgets.button import BtnApp, BtnBack
from wse.pages.widgets.text import MultilineInfoPanel


class MentoringPage(BasePage):
    """Mentoring pages."""

    _info = ''

    def __init__(self) -> None:
        """Construct the pages."""
        super().__init__()

        # Info panel
        self._info_panel = MultilineInfoPanel(value=self._info)

        # DOM
        self.add(
            self._info_panel,
            BtnApp(**self._nav.word_test),
            BtnBack(),
        )


class WordTestPage(TestLayout):
    """A vocabulary test pages."""

    url_question = urljoin(HOST, FOREIGN_TESTING_PATH)
    url_answer = urljoin(HOST, FOREIGN_TESTING_PATH)
