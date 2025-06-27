"""Defines Login container."""

from dataclasses import dataclass

import toga
from injector import inject

from wse.config.layout import LoginStyle, LoginTheme
from wse.core.interfaces.iauth import IAuthService
from wse.features.base import BaseController
from wse.features.base.container import BaseContainer
from wse.features.base.mixins import AddObserverMixin
from wse.features.interfaces import IContent, ISubject
from wse.features.subapps.nav_id import NavID
from wse.utils.i18n import _

from .interfaces import (
    ILoginContainer,
    ILoginModel,
)


@inject
class LoginModel(
    AddObserverMixin,
):
    """Login container model."""

    def __init__(
        self,
        subject: ISubject,
        auth_service: IAuthService,
    ) -> None:
        """Construct the model."""
        self._subject = subject
        self._auth_service = auth_service

    def authenticate(self, username: str, password: str) -> None:
        """Authenticate the user."""
        is_auth = self._auth_service.authenticate(username, password)

        if is_auth:
            self._handle_success_authentication()
        else:
            self._handle_error_authentication()

    def _handle_success_authentication(self) -> None: ...

    def _handle_error_authentication(self) -> None: ...


@inject
@dataclass
class LoginContainer(
    AddObserverMixin,
    BaseContainer,
):
    """Login container."""

    _subject: ISubject
    _style_config: LoginStyle
    _theme_config: LoginTheme

    def _setup(self) -> None:
        self.content.test_id = NavID.LOGIN
        self.localize()
        self.update_style(self._style_config)
        self.update_style(self._theme_config)

    def _populate_content(self) -> None:
        self.content.add(
            self._input_username,
            self._input_password,
        )

    def _create_ui(self) -> None:
        self._input_username = toga.TextInput()
        self._input_password = toga.PasswordInput()
        self._btn_confirm = toga.Button('', on_press=self._confirm_handler)

    def localize(self) -> None:
        """Localize the UI text."""
        self._input_username.placeholder = _('Username')
        self._input_password.placeholder = _('Password')

    def update_style(self, config: LoginStyle | LoginTheme) -> None:
        """Update UI style."""
        self._input_username.style.update(**config.input)
        self._input_password.style.update(**config.input)

    # Button callback functions

    def _confirm_handler(self, _: toga.Button) -> None:
        """Notify about login confirmation."""
        self._subject.notify(
            'login_confirmation',
            username=self._input_username.text,
            password=self._input_password.text,
        )


@inject
@dataclass
class LoginController(
    AddObserverMixin,
    BaseController,
):
    """Login container controller."""

    _subject: ISubject
    _model: ILoginModel
    _container: ILoginContainer

    def _setup(self) -> None:
        self._model.add_observer(self)
        self._container.add_observer(self)

    @property
    def content(self) -> IContent:
        """Get page content."""
        return self._container.content

    # Notifications

    def login_confirmation(self, username: str, password: str) -> None:
        """Handle the login confirmation."""
        self._model.confirm_login(username, password)
