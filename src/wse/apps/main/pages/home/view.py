"""Home page view of ain feature."""

from dataclasses import dataclass

import toga
from injector import inject
from typing_extensions import override

from wse.apps.nav_id import NavID
from wse.config.layout import StyleConfig, ThemeConfig
from wse.features.base import BaseView
from wse.utils.i18n import _, label_, nav_


@inject
@dataclass
class HomeView(
    BaseView,
):
    """Home page view of main feature."""

    _style: StyleConfig
    _theme: ThemeConfig

    def _setup(self) -> None:
        super()._setup()
        self._content.test_id = NavID.HOME

    def _populate_content(self) -> None:
        self._content.add(
            self._label_title,
            self._btn_math,
            self._btn_assigned,
            self._btn_login,
        )

    def _create_ui(self) -> None:
        self._label_title = toga.Label('')
        self._btn_login = self._create_nav_btn(nav_id=NavID.LOGIN)
        self._btn_logout = toga.Button(on_press=self._handle_logout)
        self._btn_math = self._create_nav_btn(nav_id=NavID.INDEX_MATH)
        self._btn_assigned = self._create_nav_btn(nav_id=NavID.ASSIGNED)

    @override
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        self._label_title.style.update(**config.label_title)
        self._btn_login.style.update(**config.btn_nav)
        self._btn_logout.style.update(**config.btn_nav)
        self._btn_math.style.update(**config.btn_nav)
        self._btn_assigned.style.update(**config.btn_nav)

    @override
    def localize_ui(self) -> None:
        """Localize the UI text."""
        self._label_title.text = label_('Home page title')
        self._btn_login.text = nav_(NavID.LOGIN)
        self._btn_logout.text = _('Logout')
        self._btn_math.text = nav_(NavID.INDEX_MATH)
        self._btn_assigned.text = nav_(NavID.ASSIGNED)

    # Button callback functions

    def _handle_logout(self, _: toga.Button) -> None:
        self._notify('logout')

    # Set content by user authentication state

    def set_authenticated_content(self) -> None:
        """Set page content for authenticated user."""
        try:
            self._content.replace(self._btn_login, self._btn_logout)
        except ValueError:
            # ignore
            pass

    def set_anonymous_content(self) -> None:
        """Set page content for anonymous user."""
        try:
            self._content.replace(self._btn_logout, self._btn_login)
        except ValueError:
            # ignore
            pass
