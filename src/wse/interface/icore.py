"""Defines protocol interfaces for application components."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

import toga

from wse.interface.ifeatures import IController

if TYPE_CHECKING:
    from wse.core.navigation.navigation_id import NavigationID


class IUser:
    """Defines the interface for user model."""


class IAuthAPI(Protocol):
    """Defines the interface for authentication-related API requests."""

    def authenticate(self, username: str, password: str) -> None:
        """Authenticate the user."""

    def validate_token(self, token: str) -> bool:
        """Validate the authentication token."""


class ISessionManager(Protocol):
    """Defines the interface for session manager."""

    def start_session(self, user: IUser, token: str) -> None:
        """Start session."""

    def end_session(self) -> None:
        """End session."""

    def is_authenticated(self) -> bool:
        """Is the user authenticated."""


class ITokenStorage(Protocol):
    """Defines the interface for authentication services."""

    def save_token(self, token: str) -> None:
        """Encrypt and save the token to a file."""

    def load_token(self) -> str | None:
        """Load and decrypt the token from a file."""


class IAuthService(Protocol):
    """Defines the interface for authentication services."""

    def authenticate(self, credentials: dict[str, str]) -> None:
        """Authenticate the user."""

    def is_authenticated(self) -> bool:
        """Check the user authentication status."""


class INavigator(Protocol):
    """Protocol defining the interface for navigator."""

    def navigate(self, navigation_id: NavigationID) -> None:
        """Navigate to page by navigation ID."""

    def set_main_window(self, main_widow: toga.Window) -> None:
        """Set the application's main window for content display."""

    @property
    def routes(self) -> dict[NavigationID, IController]:
        """Routes to get page content to window content."""

    @routes.setter
    def routes(self, value: dict[NavigationID, IController]) -> None: ...
