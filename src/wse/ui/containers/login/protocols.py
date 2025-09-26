"""Login container protocols."""

from abc import ABC, abstractmethod

from wse.config.layout import StyleConfig, ThemeConfig
from wse.feature.observer.abc import ObserverManagerABC
from wse.ui.base.container.abc import ContainerGenABC
from wse.ui.base.content.abc import GetContentABC


class LoginModelABC(
    ObserverManagerABC,
):
    """Protocol for Login container model interface."""

    def authenticate(self, username: str, password: str) -> None:
        """Authenticate the user."""


class LoginContainerABC(
    ContainerGenABC[StyleConfig, ThemeConfig],
    GetContentABC,
    ObserverManagerABC,
    ABC,
):
    """Protocol for Login container interface."""

    @abstractmethod
    def localize(self) -> None:
        """Localize the UI text."""

    @abstractmethod
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update UI style."""

    @abstractmethod
    def clear_credential(self) -> None:
        """Clear the entered credential."""


class LoginControllerProto(
    ObserverManagerABC,
    GetContentABC,
):
    """Protocol for Login container controller interface."""

    # Notifications from Container

    def login_confirm(self, username: str, password: str) -> None:
        """Handle the login confirmation."""

    def clear_credential(self) -> None:
        """Clear the entered credential."""

    def success_authentication(self) -> None:
        """Notify about successful authentication."""
