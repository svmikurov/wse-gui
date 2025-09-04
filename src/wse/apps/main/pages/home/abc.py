"""Abstract base classes for home page model."""

from abc import ABC, abstractmethod

from typing_extensions import override

from .protocols import (
    HomeModelFeatureProto,
    HomeModelObserverProto,
    HomeViewObserverProto,
)

# Model


class HomeModelFeature(ABC, HomeModelFeatureProto):
    """Abstract base class for home page model feature."""

    @abstractmethod
    @override
    def check_auth_status(self) -> None:
        """Check user authentication status."""

    @abstractmethod
    @override
    def logout(self) -> None:
        """Handle the logout event."""


class HomeModelObserver(ABC, HomeModelObserverProto):
    """Abstract base class for Home page model notification observer."""

    @abstractmethod
    @override
    def user_authenticated(self) -> None:
        """Set content for authenticated user."""

    @abstractmethod
    @override
    def user_anonymous(self) -> None:
        """Set content for anonymous user."""


# View


class HomeViewObserver(ABC, HomeViewObserverProto):
    """Abstract base class for Home page view notification observer."""

    @abstractmethod
    @override
    def logout(self) -> None:
        """Handle the logout event."""
