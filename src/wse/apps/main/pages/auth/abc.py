"""Defines abstract base class with Auth page model features."""

from abc import ABC, abstractmethod

from typing_extensions import override

from .protocols import (
    AuthModelFeatureProto,
    AuthModelObserverProto,
    AuthViewObserverProto,
)

# Model


class AuthModelFeature(ABC, AuthModelFeatureProto):
    """Abstract base class with Authentication page model features."""

    @abstractmethod
    @override
    def handle_success_authentication(self) -> None:
        """Handle the success authentication."""


class AuthModelObserver(ABC, AuthModelObserverProto):
    """Abstract base class for Model page view observer."""

    @abstractmethod
    @override
    def credential_clean(self) -> None:
        """Handle the credential clean."""


# View


class AuthViewObserver(ABC, AuthViewObserverProto):
    """Abstract base class for Auth page view notification observer."""

    @abstractmethod
    @override
    def success_authentication(self) -> None:
        """Handle the success authentication event."""
