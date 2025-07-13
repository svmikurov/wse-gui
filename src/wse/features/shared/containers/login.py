"""Defines Login container."""

import logging
from dataclasses import dataclass

import toga
from injector import inject
from typing_extensions import override

from wse.config.layout import LoginStyle, LoginTheme
from wse.core.interfaces.iauth import IAuthService
from wse.utils.i18n import _

from ...base import BaseController
from ...base.container import BaseContainer
from ...base.mixins import AddObserverMixin
from ...interfaces import IContent, ISubject
from ...shared.containers.interfaces import (
    ILoginContainer,
    ILoginController,
    ILoginModel,
)
from ...subapps.nav_id import NavID

logger = logging.getLogger(__name__)


@inject
class LoginModel(
    AddObserverMixin,
    ILoginModel,
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

    @override
    def authenticate(self, username: str, password: str) -> None:
        """Authenticate the user."""
        # Request the authentication
        is_auth = self._auth_service.authenticate(username, password)

        if is_auth:
            self._handle_success_authentication()
        else:
            self._handle_error_authentication()

    def _handle_success_authentication(self) -> None:
        self._notify_success_authentication()

    def _handle_error_authentication(self) -> None:
        pass

    # Notifications

    def _notify_success_authentication(self) -> None:
        self._subject.notify('success_authentication')


@inject
@dataclass
class LoginContainer(
    AddObserverMixin,
    BaseContainer,
    ILoginContainer,
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
            self._btn_confirm,
        )

    def _create_ui(self) -> None:
        self._input_username = toga.TextInput()
        self._input_password = toga.PasswordInput()
        self._btn_confirm = toga.Button('', on_press=self._confirm_handler)

    @override
    def localize(self) -> None:
        """Localize the UI text."""
        self._input_username.placeholder = _('Username')
        self._input_password.placeholder = _('Password')
        self._btn_confirm.text = _('Login')

    @override
    def update_style(self, config: LoginStyle | LoginTheme) -> None:
        """Update UI style."""
        self._input_username.style.update(**config.input)
        self._input_password.style.update(**config.input)
        self._btn_confirm.style.update(**config.button)

    @override
    def clear_credential(self) -> None:
        """Clear the entered credential."""
        self._input_username.value = ''
        self._input_password.value = ''

    # Button callback functions

    def _confirm_handler(self, _: toga.Button) -> None:
        """Notify about login confirmation."""
        self._subject.notify(
            'login_confirm',
            username=self._input_username.value,
            password=self._input_password.value,
        )


@inject
@dataclass
class LoginController(
    AddObserverMixin,
    BaseController,
    ILoginController,
):
    """Login container controller."""

    _subject: ISubject
    _model: ILoginModel
    _container: ILoginContainer

    @override
    def _setup(self) -> None:
        self._model.add_observer(self)
        self._container.add_observer(self)

    @override
    @property
    def content(self) -> IContent:
        """Get page content."""
        return self._container.content

    @override
    def clear_credential(self) -> None:
        """Clear the entered credential."""
        self._container.clear_credential()

    # Notifications from Container

    @override
    def login_confirm(self, username: str, password: str) -> None:
        """Handle the login confirmation."""
        self._model.authenticate(username, password)

    @override
    def success_authentication(self) -> None:
        """Notify about successful authentication."""
        self._subject.notify('success_authentication')
