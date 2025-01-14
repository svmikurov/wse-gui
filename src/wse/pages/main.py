"""Main box."""

from http import HTTPStatus
from urllib.parse import urljoin

import toga
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
    request_user_data,
)
from wse.pages.handlers.goto_handler import (
    goto_foreign_exercise_handler,
    goto_foreign_main_handler,
    goto_glossary_exercise_handler,
    goto_glossary_main_handler,
    goto_login_handler,
)
from wse.pages.widgets.box_page import BaseBox, WidgetMixin
from wse.pages.widgets.button import BtnApp
from wse.pages.widgets.label import TitleLabel
from wse.sources.text_panel_main import SourceMainPanel
from wse.sources.user import SourceUser


class MainBox(WidgetMixin, BaseBox):
    """Main box."""

    welcome = f'Ready for connect to {HOST}'
    url_logout = urljoin(HOST, LOGOUT_PATH)
    """User logout url, allowed POST method (`str`).
    """

    def __init__(
        self,
        user: SourceUser,
        source_info_panel: SourceMainPanel,
    ) -> None:
        """Construct the Main box."""
        super().__init__()
        self.user = user
        self.source_main_panel = source_info_panel
        self._index_btn_auth = 2

        # Title.
        self.label_title = TitleLabel(TITLE_MAIN)

        # Buttons.
        self.btn_goto_login = BtnApp(
            BTN_GOTO_LOGIN,
            on_press=goto_login_handler,
        )
        self.btn_logout = BtnApp(
            BTN_LOGOUT,
            on_press=self.logout_handler,
        )
        self.btn_goto_glossary_main = BtnApp(
            BTN_GOTO_GLOSSARY_MAIN,
            on_press=goto_glossary_main_handler,
        )
        self.btn_goto_foreign_main = BtnApp(
            BTN_GOTO_FOREIGN_MAIN,
            on_press=goto_foreign_main_handler,
        )

        # Quick start of exercise, buttons.
        self.label_chapter_exercises = toga.Label(
            'Упражнения:',
            style=Pack(padding=(4, 0, 2, 2)),
        )
        self.btn_goto_foreign_exercise = BtnApp(
            'Изучение слов',
            on_press=goto_foreign_exercise_handler,
        )
        self.btn_goto_glossary_exercise = BtnApp(
            'Изучение терминов',
            on_press=goto_glossary_exercise_handler,
        )

        # Info panel
        self.info_panel = toga.MultilineTextInput(
            readonly=True,
            style=Pack(flex=1),
            value=self.welcome,
        )

        # DOM.
        self.add(
            self.label_title,
            self.info_panel,
            self.btn_goto_login,
            self.btn_goto_foreign_main,
            self.btn_goto_glossary_main,
        )

    async def on_open(self, widget: toga.Widget) -> None:
        """Update widgets."""
        if app_auth.token:
            response = request_user_data()

            if response.status_code == HTTPStatus.OK and not self.user.is_auth:
                payload = response.json()
                self.user.set_userdata(payload)
                self.user.save_userdata(payload)

            elif response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
                self.user.is_auth = False

            self.update_widgets()

    async def logout_handler(self, _: toga.Widget) -> None:
        """Send the http request to log out, button handler."""
        response = request_post(url=self.url_logout)

        if response.status_code == HTTPStatus.NO_CONTENT:
            del app_auth.token
            self.user.delete_userdata()
            self.update_widgets()

    def update_widgets(self) -> None:
        """Update widgets by user auth status."""
        if self.user.is_auth:
            self.place_logout_button()
            self.display_userdata()
        else:
            self.place_login_button()
            self.display_greetings()

    def place_login_button(self) -> None:
        """Place login buttons."""
        try:
            self.replace(self.btn_logout, self.btn_goto_login)
        except ValueError:
            # The button is already placed.
            pass

    def place_logout_button(self) -> None:
        """Place logout buttons."""
        try:
            self.replace(self.btn_goto_login, self.btn_logout)
        except ValueError:
            # The button is already placed.
            pass

    def display_userdata(self) -> None:
        """Display the user data."""
        self.info_panel.value = 'Добро пожаловать, {}!'.format(
            self.user.username
        )

    def display_greetings(self) -> None:
        """Display greetings."""
        self.info_panel.value = self.welcome
