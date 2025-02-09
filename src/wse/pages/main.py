"""Main box."""

import toga

from wse.constants import STYLE_BTN_CANCEL, STYLE_BTN_CONFIRM
from wse.pages.base import BasePage
from wse.pages.widgets import BtnApp, InfoPanel


class HomePage(BasePage):
    """Home pages."""

    title = 'WSELFEDU'

    def __init__(self) -> None:
        """Construct the pages."""
        super().__init__()

        # Info panel
        self.info_panel = InfoPanel()

        # Auth buttons
        self.btn_goto_login = BtnApp(**self._nav.login)
        # The callback function is assigned by the controller.
        self.btn_logout = BtnApp('Выйти из учетной записи')
        self.btn_logout_cancel = BtnApp('Отмена', style=STYLE_BTN_CANCEL)
        self.btn_logout_confirm = BtnApp('Выйти', style=STYLE_BTN_CONFIRM)

        # Auth buttons container
        self.box_auth_btn = toga.Box()

        # DOM
        self.add(
            self.info_panel,
            self.box_auth_btn,
            BtnApp(**self._nav.foreign_main),
            BtnApp(**self._nav.glossary_main),
            BtnApp(**self._nav.math_main),
            BtnApp(**self._nav.mentoring),
            BtnApp(**self._nav.explorer_main),
        )

    async def on_open(self, widget: toga.Widget) -> None:
        """Invoke methods on page open."""
        await self._contr.on_open(widget)
