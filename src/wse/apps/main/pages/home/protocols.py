"""Protocols for Home page components interface."""

from typing import Any, Protocol

from wse.feature.interfaces.imvc import (
    ModelProto,
    PageControllerProto,
    ViewProto,
)

# Model


class HomeModelFeatureProto(Protocol):
    """Protocol for home page model feature interface."""

    def check_auth_status(self) -> None:
        """Check user authentication status."""

    def logout(self) -> None:
        """Handle the logout event."""


class HomeModelProto(HomeModelFeatureProto, ModelProto):
    """Protocol for Home page model interface."""


class HomeModelObserverProto(Protocol):
    """Protocol for Home page model notification observer interface."""

    def user_authenticated(self) -> None:
        """Set content for authenticated user."""

    def user_anonymous(self) -> None:
        """Set content for anonymous user."""


# View


class HomeViewProto(HomeModelObserverProto, ViewProto):
    """Protocol for Home page view interface."""


class HomeViewObserverProto(Protocol):
    """Protocol for Home page view notification observer interface."""

    def logout(self) -> None:
        """Handle the logout event."""


# Controller


class HomeControllerProto(PageControllerProto[Any]):
    """Protocol for Home page controller interface."""
