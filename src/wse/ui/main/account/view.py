"""Account View."""

from dataclasses import dataclass

import toga
from injector import inject
from typing_extensions import override

from wse.config.layout import StyleConfig, ThemeConfig
from wse.core.navigation.nav_id import NavID
from wse.feature.shared.containers.login import LoginControllerProto
from wse.feature.shared.containers.top_bar.abc import TopBarControllerABC
from wse.utils.i18n import label_, nav_

from ...base.mixin import NavigateViewMixin
from .abc import AuthViewABC, AuthViewModelABC


@inject
@dataclass
class AuthView(
    NavigateViewMixin,
    AuthViewABC,
):
    """Account View."""

    _state: AuthViewModelABC

    # Widget injection
    _top_bar: TopBarControllerABC
    _login_container: LoginControllerProto

    @override
    def __post_init__(self) -> None:
        """Construct the view."""
        super().__post_init__()
        self.content.test_id = NavID.LOGIN
        self._top_bar.add_observer(self)
        self._login_container.add_observer(self)
        self._state.add_observer(self)

    @override
    def _populate_content(self) -> None:
        self.content.add(
            self._top_bar.content,
            self._label_title,
            self._btn_logout,
        )

    @override
    def _create_ui(self) -> None:
        self._label_title = toga.Label('')
        self._btn_logout = toga.Button(on_press=self._state.logout)

    @override
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        self._label_title.style.update(**config.label_title)
        self._btn_logout.style.update(**config.btn_nav)

    @override
    def localize_ui(self) -> None:
        """Localize the UI text."""
        self._label_title.text = label_('Login page title')
        self._btn_logout.text = nav_(NavID.LOGOUT)

    def on_open(self) -> None:
        """Call methods on page open."""
        self._state.refresh_context()

    # Login container observe

    def success_authentication(self) -> None:
        """Handle success authentication event."""
        self._state.handle_success_authentication()

    # ViewModel observe

    @override
    def user_authenticated(self) -> None:
        """Set content for authenticated user."""
        try:
            self._content.replace(
                self._login_container.content, self._btn_logout
            )
        except ValueError:
            # Content for authenticated user is already set
            pass

    @override
    def user_anonymous(self) -> None:
        """Set content for anonymous user."""
        try:
            self._content.replace(
                self._btn_logout, self._login_container.content
            )
        except ValueError:
            # Content for anonymous user is already set
            pass

    # On screen close event

    def on_close(self) -> None:
        """Call methods before close the screen."""
        self._top_bar.remove_observer(self)
        self._login_container.remove_observer(self)
        self._state.remove_observer(self)
        self._state.on_close()
