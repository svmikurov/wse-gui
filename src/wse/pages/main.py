"""Main box."""

from http import HTTPStatus
from urllib.parse import urljoin

import toga
from toga.style import Pack

from wse.constants import (
    BTN_LOGOUT,
    HOST,
    LOGOUT_PATH,
    TITLE_MAIN,
)
from wse.constants.settings import STYLE_BTN_CANCEL, STYLE_BTN_CONFIRM
from wse.contrib.http_requests import (
    app_auth,
    request_auth_data,
    request_post,
)
from wse.controllers.goto import GoToContr
from wse.models.user import SourceUser
from wse.pages.base import BasePage
from wse.pages.widgets.box_page import BaseBox, WidgetMixin
from wse.pages.widgets.button import BtnApp
from wse.pages.widgets.label import TitleLabel
from wse.pages.widgets.text_input import InfoPanel, InfoTextPanel
from wse.sources.text_panel_main import SourceMainPanel


class MainPage(BasePage):
    """Main pages."""

    title = TITLE_MAIN

    def __init__(self) -> None:
        """Construct the pages."""
        super().__init__()

        # Info panel
        self._info_panel = InfoPanel()

        # Navigation buttons
        self._btn_goto_login = BtnApp(**self._goto.login)
        self._btn_goto_foreign_main = BtnApp(**self._goto.foreign_main)
        self._btn_goto_glossary_main = BtnApp(**self._goto.glossary_main)
        self._btn_goto_math_main = BtnApp(**self._goto.math_main)
        self._btn_goto_mentoring = BtnApp(**self._goto.mentoring)
        self._btn_goto_explorer = BtnApp(**self._goto.explorer_main)

        # DOM
        self.add(
            self._info_panel,
            self._btn_goto_login,
            self._btn_goto_foreign_main,
            self._btn_goto_glossary_main,
            self._btn_goto_math_main,
            self._btn_goto_mentoring,
            self._btn_goto_explorer,
        )


class MainBox(WidgetMixin, BaseBox):
    """Main box."""

    _welcome = f'Ready for connect to {HOST}'
    _url_logout = urljoin(HOST, LOGOUT_PATH)

    def __init__(
        self,
        user: SourceUser,
        source_info_panel: SourceMainPanel,
    ) -> None:
        """Construct the Main box."""
        super().__init__()
        self._user = user
        self._source_main_panel = source_info_panel
        self._index_btn_auth = 2

        self._goto = GoToContr()

        self._label_title = TitleLabel(TITLE_MAIN)

        # Info panel
        self._info_panel = InfoTextPanel(
            style=Pack(flex=1), value=self._welcome
        )

        # Navigation buttons
        self._btn_goto_login = BtnApp(**self._goto.login)
        self._btn_logout = BtnApp(
            BTN_LOGOUT, on_press=self._display_logout_handler
        )
        self._btn_goto_mentoring = BtnApp(**self._goto.mentoring)
        self._btn_goto_glossary_main = BtnApp(**self._goto.glossary_main)
        self._btn_goto_foreign_main = BtnApp(**self._goto.foreign_main)
        self._btn_goto_math_main = BtnApp(**self._goto.math_main)
        self._btn_goto_explorer = BtnApp(**self._goto.explorer_main)

        # Confirm buttons
        self._btn_logout_cancel = BtnApp(
            'Отмена',
            style=STYLE_BTN_CANCEL,
            on_press=self._undisplay_logout_handler,
        )
        self._btn_logout_confirm = BtnApp(
            'Выйти',
            style=STYLE_BTN_CONFIRM,
            on_press=self._confirm_logout_handler,
        )

        # Boxes
        self._box_logout_confirm = toga.Box(
            children=[self._btn_logout_cancel, self._btn_logout_confirm]
        )

        # DOM
        self.add(
            self._label_title,
            self._info_panel,
            self._btn_goto_login,
            self._btn_goto_mentoring,
            self._btn_goto_foreign_main,
            self._btn_goto_math_main,
            self._btn_goto_glossary_main,
            self._btn_goto_explorer,
        )

    async def on_open(self, _: toga.Widget) -> None:
        """Update widgets."""
        if app_auth.token:
            response = request_auth_data()

            if (
                response.status_code == HTTPStatus.OK
                and not self._user.is_auth
            ):
                payload = response.json()
                self._user.set_userdata(payload)
                self._user.save_userdata(payload)

            elif response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
                self._user.is_auth = False

            self.update_widgets()

    #####################################################################
    # Button handlers

    async def _logout_handler(self, _: toga.Widget) -> None:
        """Send the http request to log out, button handler."""
        response = request_post(url=self._url_logout)

        if response.status_code == HTTPStatus.NO_CONTENT:
            del app_auth.token
            self._user.delete_userdata()
            self.update_widgets()

    #####################################################################
    # Construct pages methods

    def update_widgets(self) -> None:
        """Update widgets by user auth status."""
        if self._user.is_auth:
            self._place_logout_button()
            self._display_userdata()
        else:
            self._place_login_button()
            self._display_greetings()

    def _place_login_button(self) -> None:
        try:
            self.replace(self._btn_logout, self._btn_goto_login)
        except ValueError:
            # The button is already placed.
            pass

    def _place_logout_button(self) -> None:
        try:
            self.replace(self._btn_goto_login, self._btn_logout)
        except ValueError:
            # The button is already placed.
            pass

    def _display_userdata(self) -> None:
        self._info_panel.value = 'Добро пожаловать, {}!'.format(
            self._user.username
        )

    def _display_greetings(self) -> None:
        self._info_panel.value = self._welcome

    ##################
    # Confirm handlers

    def _display_logout_handler(self, _: toga.Widget) -> None:
        self.replace(self._btn_logout, self._box_logout_confirm)

    def _undisplay_logout_handler(self, _: toga.Widget) -> None:
        self.replace(self._box_logout_confirm, self._btn_logout)

    async def _confirm_logout_handler(self, widget: toga.Widget) -> None:
        await self._logout_handler(widget)
        # TODO: Refactor: remove _undisplay_logout_handler method.
        self._undisplay_logout_handler(widget)
        self._place_login_button()
