"""Main box."""

import toga

from wse.constants.settings import STYLE_BTN_CANCEL, STYLE_BTN_CONFIRM
from wse.pages.base import BasePage
from wse.pages.widgets.button import BtnApp
from wse.pages.widgets.text_input import InfoPanel


class MainPage(BasePage):
    """Main pages."""

    title = 'WSELFEDU'

    def __init__(self) -> None:
        """Construct the pages."""
        super().__init__()

        # Info panel
        self.info_panel = InfoPanel()

        # Navigation buttons
        self.btn_goto_login = BtnApp(**self._nav.login)
        self._btn_goto_foreign_main = BtnApp(**self._nav.foreign_main)
        self._btn_goto_glossary_main = BtnApp(**self._nav.glossary_main)
        self._btn_goto_math_main = BtnApp(**self._nav.math_main)
        self._btn_goto_mentoring = BtnApp(**self._nav.mentoring)
        self._btn_goto_explorer = BtnApp(**self._nav.explorer_main)

        # Logout buttons
        self.btn_logout = BtnApp('Выйти из учетной записи')
        self.btn_logout_cancel = BtnApp('Отмена', style=STYLE_BTN_CANCEL)
        self.btn_logout_confirm = BtnApp('Выйти', style=STYLE_BTN_CONFIRM)

        # Inner boxes
        self.box_auth_btn = toga.Box()

        # DOM
        self.add(
            self.info_panel,
            self.box_auth_btn,
            self._btn_goto_foreign_main,
            self._btn_goto_glossary_main,
            self._btn_goto_math_main,
            self._btn_goto_mentoring,
            self._btn_goto_explorer,
        )

    async def on_open(self, widget: toga.Widget) -> None:
        """Invoke methods on page open."""
        await self._contr.on_open(widget)
