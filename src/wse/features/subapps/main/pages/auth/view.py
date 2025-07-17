"""Defines Authentication page view."""

from dataclasses import dataclass

import toga
from injector import inject
from typing_extensions import override

from wse.config.layout import StyleConfig, ThemeConfig
from wse.features.base import BaseView
from wse.features.interfaces.iwidgets import INavButton
from wse.features.shared.containers.interfaces import ILoginController
from wse.features.subapps.nav_id import NavID
from wse.utils.i18n import label_, nav_


@inject
@dataclass
class AuthView(
    BaseView,
):
    """Authentication page view."""

    _login_container: ILoginController

    @override
    def _setup(self) -> None:
        super()._setup()
        self.content.test_id = NavID.LOGIN
        self._login_container.add_observer(self)

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

    # API for controller

    def clear_credential(self) -> None:
        """Clear the entered credential."""
        self._login_container.clear_credential()

    # Notifications from Login container

    def success_authentication(self) -> None:
        """Notify subjects about success authentication event."""
        self._notify('success_authentication')

    # Button callback functions

    def _handle_navigate(self, button: INavButton) -> None:
        """Handle navigation button press."""
        self.clear_credential()
        super()._handle_navigate(button)
