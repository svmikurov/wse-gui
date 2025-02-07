"""User data source."""

import json
import os
from http import HTTPStatus
from pathlib import Path
from urllib.parse import urljoin

from toga.sources import Source

from wse.constants import (
    HOST,
    LOGOUT_PATH,
    USER_DATA_PATH,
)
from wse.contrib.http_requests import (
    app_auth,
    request_auth_data,
    request_get,
    request_post,
)

PATH_USERDATA_FILE = os.path.join(
    Path(__file__).parent.parent,
    'resources/userdata.json',
)


# TODO: Split class into parents by responsibilities.
class User(Source):
    """User data source."""

    _url_user_data = urljoin(HOST, USER_DATA_PATH)
    _url_logout = urljoin(HOST, LOGOUT_PATH)

    def __init__(self) -> None:
        """Construct the source."""
        super().__init__()
        self._username: str | None = None
        self._point_balance: str | None = None

    def on_open(self) -> None:
        """Set user data on start app."""
        if self.is_auth:
            self._set_auth_data()
            self._set_user_data()
            self._place_auth_widgets()
        else:
            self._place_unauth_widgets()

        self._display_data(self.greeting)
        self._update_info_panel()

    def logout(self) -> None:
        """Logout."""
        response = request_post(url=self._url_logout)

        if response.status_code == HTTPStatus.NO_CONTENT:
            del app_auth.token
            self.delete_userdata()
            self._place_unauth_widgets()
            self._display_data(self.greeting)

    ####################################################################
    # User data

    @property
    def username(self) -> str:
        """The username (`str`)."""
        return self._username

    @property
    def is_auth(self) -> bool:
        """The user auth status (`bool`)."""
        response = request_auth_data()
        if response.status_code == HTTPStatus.OK:
            return True
        return False

    def set_userdata(self, userdata: dict) -> None:
        """Set user source."""
        self._username = userdata.get('username')

    @staticmethod
    def save_userdata(userdata: dict) -> None:
        """Save user data."""
        with open(PATH_USERDATA_FILE, 'w', encoding='utf-8') as fp:
            json.dump(userdata, fp, ensure_ascii=False, indent=4)

    def delete_userdata(self) -> None:
        """Delete user data."""
        self._username = None
        self._delete_userdata_fail()

    @staticmethod
    def _delete_userdata_fail() -> None:
        try:
            os.unlink(PATH_USERDATA_FILE)
        except FileNotFoundError:
            pass

    def _load_userdata(self) -> None:
        try:
            with open(PATH_USERDATA_FILE, 'r') as file:
                userdata = json.load(file)
        except FileNotFoundError:
            print('INFO: User data was not saved')
            pass
        else:
            self.set_userdata(userdata)

    ####################################################################
    # Notifications

    def _display_data(self, data: dict) -> None:
        self.notify('display_data', data=data)

    def _place_auth_widgets(self) -> None:
        self.notify('place_auth_widgets')

    def _place_unauth_widgets(self) -> None:
        self.notify('place_unauth_widgets')

    def _update_info_panel(self) -> None:
        self.notify('update_info_panel', text=self.info)

    ####################################################################
    # Data

    @property
    def greeting(self) -> dict[str, str]:
        """App greeting."""
        key = 'greetings'
        data = {key: f'Добро пожаловать, {self.username}!'}
        if not self.username:
            data[key] = f'Ready for connect to {HOST}'
        return data

    @property
    def info(self) -> str:
        """User points."""
        data = f'Баланс: {self._point_balance}'
        return data

    ####################################################################
    # HTTP requests

    def _set_auth_data(self) -> None:
        response = request_auth_data()

        if response.status_code == HTTPStatus.OK:
            userdata = response.json()
            self.set_userdata(userdata)
            self.save_userdata(userdata)

        elif response.status_code == HTTPStatus.UNAUTHORIZED:
            self.delete_userdata()
            del app_auth.token

    def _set_user_data(self) -> None:
        response = request_get(self._url_user_data)
        data = response.json()
        self._point_balance = data.get('point_balance')
