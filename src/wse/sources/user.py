"""User data source."""

import json
import os
from http import HTTPStatus
from pathlib import Path

from toga.sources import Source

from wse.contrib.http_requests import app_auth, request_auth_data

PATH_USERDATA_FILE = os.path.join(
    Path(__file__).parent.parent,
    'resources/userdata.json',
)


class SourceUser(Source):
    """User data source."""

    def __init__(self) -> None:
        """Construct the source."""
        super().__init__()
        self._username: str | None = None
        self._is_auth: bool = False
        self._points: str | None = None

    @property
    def username(self) -> str:
        """The username (`str`)."""
        return self._username

    @property
    def is_auth(self) -> bool:
        """The user auth status (`bool`)."""
        return self._is_auth

    @is_auth.setter
    def is_auth(self, value: bool) -> None:
        self._is_auth = value

    def set_userdata(self, userdata: dict) -> None:
        """Set user source."""
        self._username = userdata.get('username')
        self._is_auth = True if self._username else False

    @staticmethod
    def save_userdata(userdata: dict) -> None:
        """Save user data."""
        with open(PATH_USERDATA_FILE, 'w', encoding='utf-8') as fp:
            json.dump(userdata, fp, ensure_ascii=False, indent=4)

    def delete_userdata(self) -> None:
        """Delete user data."""
        self._username = None
        self._is_auth = False
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

    def on_start(self) -> None:
        """Set user data on start app."""
        response = request_auth_data()

        if response.status_code == HTTPStatus.OK:
            userdata = response.json()
            self.set_userdata(userdata)
            self.save_userdata(userdata)

        elif response.status_code == HTTPStatus.UNAUTHORIZED:
            self.delete_userdata()
            del app_auth.token
