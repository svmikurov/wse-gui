"""Login box-container."""

from http import HTTPStatus

import toga
from toga.style import Pack

from wse.constants import (
    BTN_LOGIN,
    CONNECTION_ERROR_MSG,
    INPUT_HEIGHT,
    LOGIN_PATH,
)
from wse.constants.settings import CONNECTION_BAD_MSG, CONNECTION_SUCCESS_MSG
from wse.contrib.http_requests import obtain_token, request_auth_data
from wse.models.user import User
from wse.pages.base import BasePage
from wse.pages.handlers.goto_handler import goto_main_handler
from wse.pages.widgets.box_page import WidgetMixin
from wse.pages.widgets.button import BtnApp, BtnBack


class LoginBox(WidgetMixin, BasePage):
    """Credentials input widgets container."""

    title = 'Вход в учетную запись'
    url_path = LOGIN_PATH

    def __init__(self, user: User) -> None:
        """Construct the widgets."""
        super().__init__()
        self.user = user

        # Styles.
        style_input = Pack(height=INPUT_HEIGHT)

        # Widgets.
        # fmt: off
        self.input_username = toga.TextInput(placeholder='Имя', style=style_input)  # noqa: E501
        self.input_password = toga.PasswordInput(placeholder='Пароль', style=style_input)  # noqa: E501
        self.btn_login = BtnApp(BTN_LOGIN, on_press=self.login_handler)
        # fmt: on

        # Widgets DOM.
        self.add(
            self.input_username,
            self.input_password,
            self.btn_login,
            BtnBack(),
        )

    async def on_open(self, widget: toga.Widget) -> None:
        """Clear fields."""
        self._clear_input_fields()

    async def login_handler(self, widget: toga.Widget) -> None:
        """Submit login, button handler."""
        credentials = self.get_credentials()

        if credentials:
            response_token = obtain_token(credentials)

            if response_token.status_code == HTTPStatus.OK:
                response_userdata = request_auth_data()

                if response_userdata.status_code == HTTPStatus.OK:
                    payload = response_userdata.json()
                    # Save user data.
                    self.user.set_userdata(payload)
                    self.user.save_userdata(payload)

                    # Update widgets.
                    self._clear_input_fields()
                    # widget.root.app.page_main.update_widgets()
                    await goto_main_handler(widget)

                    # Display success message.
                    await self.show_message(*CONNECTION_SUCCESS_MSG)

            # Display error message.
            elif (
                response_token.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
            ):
                await self.show_message(*CONNECTION_ERROR_MSG)

            # Display error message if username or password.
            elif response_token.status_code == HTTPStatus.BAD_REQUEST:
                await self.show_message(*CONNECTION_BAD_MSG)

        else:
            # TODO: Add error message
            pass

    def get_credentials(self) -> dict | None:
        """Extract user data from form."""
        username = self.input_username.value
        password = self.input_password.value

        if username and password:
            return {'username': username, 'password': password}
        else:
            print('INFO: введены не полные данные для входа в учетную запись')

    def _clear_input_fields(self) -> None:
        """Clear the fields with credentials."""
        self.input_username.value = None
        self.input_password.value = None
