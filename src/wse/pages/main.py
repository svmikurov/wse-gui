"""Main box."""

from http import HTTPStatus
from urllib.parse import urljoin

import toga
from toga import colors
from toga.style import Pack

from wse.constants import (
    BTN_GOTO_FOREIGN_MAIN,
    BTN_GOTO_GLOSSARY_MAIN,
    BTN_GOTO_LOGIN,
    BTN_LOGOUT,
    HOST,
    LOGOUT_PATH,
    TITLE_MAIN,
)
from wse.contrib.http_requests import (
    app_auth,
    request_post,
    request_auth_data,
)
from wse.pages.handlers.goto_handler import (
    goto_explorer_handler,
    goto_foreign_main_handler,
    goto_glossary_main_handler,
    goto_login_handler,
    goto_mathematics_main_handler,
    goto_mentoring_handler,
)
from wse.pages.widgets.box_page import BaseBox, WidgetMixin
from wse.pages.widgets.button import BtnApp
from wse.pages.widgets.label import TitleLabel
from wse.pages.widgets.text_input import InfoTextPanel
from wse.sources.text_panel_main import SourceMainPanel
from wse.sources.user import SourceUser


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

        self._label_title = TitleLabel(TITLE_MAIN)

        # Info panel
        self._info_panel = InfoTextPanel(
            style=Pack(flex=1), value=self._welcome
        )

        # Navigation buttons
        self._btn_goto_login = BtnApp(
            BTN_GOTO_LOGIN, on_press=goto_login_handler
        )
        self._btn_logout = BtnApp(
            BTN_LOGOUT, on_press=self._display_logout_handler
        )
        self._btn_goto_mentoring = BtnApp(
            'Выполнение заданий', on_press=goto_mentoring_handler
        )
        self._btn_goto_glossary_main = BtnApp(
            BTN_GOTO_GLOSSARY_MAIN, on_press=goto_glossary_main_handler
        )
        self._btn_goto_foreign_main = BtnApp(
            BTN_GOTO_FOREIGN_MAIN, on_press=goto_foreign_main_handler
        )
        self._btn_goto_mathematics_main = BtnApp(
            'Математика', on_press=goto_mathematics_main_handler
        )
        self._btn_goto_explorer = BtnApp(
            'Изучение виджетов', on_press=goto_explorer_handler
        )
        # Confirm buttons
        self._btn_logout_cancel = BtnApp(
            'Отмена',
            style=Pack(background_color=colors.TOMATO),
            on_press=self._undisplay_logout_handler,
        )
        self._btn_logout_confirm = BtnApp(
            'Выйти',
            style=Pack(background_color=colors.GREEN),
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
            self._btn_goto_mathematics_main,
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
    # Construct page methods

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
