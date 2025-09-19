"""Login container protocols."""

from typing import Protocol

from wse.config.layout import StyleConfig, ThemeConfig
from wse.feature.interfaces.icontainer import Containerizable
from wse.feature.interfaces.icontent import GetContentProto
from wse.feature.interfaces.iobserver import AddObserverProto


class LoginModelProto(
    AddObserverProto,
    Protocol,
):
    """Protocol for Login container model interface."""

    def authenticate(self, username: str, password: str) -> None:
        """Authenticate the user."""


class LoginContainerProto(
    AddObserverProto,
    Containerizable,
    Protocol,
):
    """Protocol for Login container interface."""

    def localize(self) -> None:
        """Localize the UI text."""

    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update UI style."""

    def clear_credential(self) -> None:
        """Clear the entered credential."""


class LoginControllerProto(
    AddObserverProto,
    GetContentProto,
    Protocol,
):
    """Protocol for Login container controller interface."""

    # Notifications from Container

    def login_confirm(self, username: str, password: str) -> None:
        """Handle the login confirmation."""

    def clear_credential(self) -> None:
        """Clear the entered credential."""

    def success_authentication(self) -> None:
        """Notify about successful authentication."""
