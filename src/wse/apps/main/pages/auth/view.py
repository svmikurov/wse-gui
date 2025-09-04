"""Defines Authentication page view."""

from dataclasses import dataclass
from typing import Literal

import toga
from injector import inject
from typing_extensions import override

from wse.apps.main.pages.auth.abc import AuthModelObserver
from wse.apps.nav_id import NavID
from wse.config.layout import StyleConfig, ThemeConfig
from wse.feature.base import View
from wse.feature.base.mixins import AddObserverGeneric, CreateNavButtonMixin
from wse.feature.interfaces.iwidgets import NavButtonProto
from wse.feature.shared.containers.login import (
    LoginControllerProto,
    LoginObserver,
)
from wse.utils.i18n import label_, nav_

_NotifyType = Literal['success_authentication']


class _Utility:
    """Mixing providing utility methods for view."""

    _login_container: LoginControllerProto

    def _clear_credential(self) -> None:
        """Clear the entered credential."""
        self._login_container.clear_credential()


class _ModelObserver(
    _Utility,
    AuthModelObserver,
):
    """Mixin providing observe to Auth page model event."""

    @override
    def credential_clean(self) -> None:
        """Handle the credential clean."""
        self._clear_credential()


class _LoginContainerObserver(
    LoginObserver,
    AddObserverGeneric[_NotifyType],
):
    """Mixin providing observe to Login container event."""

    @override
    def success_authentication(self) -> None:
        """Notify subjects about success authentication event."""
        self._notify('success_authentication')


class _Callback(
    _Utility,
    CreateNavButtonMixin,
):
    """Mixin providing callback functions."""

    def _handle_navigate(self, button: NavButtonProto) -> None:
        """Handle navigation button press."""
        self._clear_credential()
        super()._handle_navigate(button)


@inject
@dataclass
class AuthView(
    _ModelObserver,
    _LoginContainerObserver,
    _Callback,
    _Utility,
    LoginObserver,
    View,
):
    """Authentication page view."""

    _login_container: LoginControllerProto

    @override
    def __post_init__(self) -> None:
        """Construct the view."""
        super().__post_init__()
        self._login_container.add_observer(self)
        self.content.test_id = NavID.LOGIN

    @override
    def _populate_content(self) -> None:
        self.content.add(
            self._label_title,
            self._login_container.content,
            self._btn_back,
        )

    @override
    def _create_ui(self) -> None:
        self._label_title = toga.Label('')
        self._btn_back = self._create_nav_btn(NavID.BACK)

    @override
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        self._label_title.style.update(**config.label_title)
        self._btn_back.style.update(**config.btn_nav)

    @override
    def localize_ui(self) -> None:
        """Localize the UI text."""
        self._label_title.text = label_('Login page title')
        self._btn_back.text = nav_(NavID.BACK)
