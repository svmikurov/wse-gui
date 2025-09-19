"""Defines Login container."""

import logging
from dataclasses import dataclass

import toga
from injector import inject
from typing_extensions import override

from wse.config.layout import StyleConfig, ThemeConfig
from wse.core.auth import AuthServiceProto
from wse.core.navigation.nav_id import NavID
from wse.feature.base import Controller
from wse.feature.base.mixins import AddObserverMixin
from wse.feature.interfaces.icontent import ContentProto
from wse.feature.interfaces.iobserver import SubjectABC
from wse.ui.base.abc.container import AddContentABC
from wse.ui.containers.login import (
    LoginContainerProto,
    LoginModelProto,
)
from wse.utils.i18n import _

logger = logging.getLogger(__name__)


@inject
class LoginModel(
    AddObserverMixin,
    LoginModelProto,
):
    """Login container model."""

    def __init__(
        self,
        subject: SubjectABC,
        auth_service: AuthServiceProto,
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
    AddContentABC,
):
    """Login container."""

    _subject: SubjectABC
    _style: StyleConfig
    _theme: ThemeConfig

    def _setup(self) -> None:
        self.content.test_id = NavID.LOGIN
        self.localize_ui()
        self.update_style(self._style)
        self.update_style(self._theme)

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

    def localize_ui(self) -> None:
        """Localize the UI text."""
        self._input_username.placeholder = _('Username')
        self._input_password.placeholder = _('Password')
        self._btn_confirm.text = _('Login')

    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update UI style."""
        self._input_username.style.update(**config.login.input)
        self._input_password.style.update(**config.login.input)
        self._btn_confirm.style.update(**config.button)

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
    Controller,
):
    """Login container controller."""

    _subject: SubjectABC
    _model: LoginModelProto
    _container: LoginContainerProto

    @override
    def _setup(self) -> None:
        self._model.add_observer(self)
        self._container.add_observer(self)

    @override
    @property
    def content(self) -> ContentProto:
        """Get page content."""
        return self._container.content

    def clear_credential(self) -> None:
        """Clear the entered credential."""
        self._container.clear_credential()

    # Notifications from Container

    def login_confirm(self, username: str, password: str) -> None:
        """Handle the login confirmation."""
        self._model.authenticate(username, password)

    def success_authentication(self) -> None:
        """Notify about successful authentication."""
        self._subject.notify('success_authentication')
