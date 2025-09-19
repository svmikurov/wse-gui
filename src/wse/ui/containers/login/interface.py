"""Login controller interface.

Use ``LoginFeatureInterface`` to invoke a feature of Login container.

Use ``LoginObserverABC`` to define methods for listing Login container
notifications.
"""

from abc import ABC, abstractmethod
from typing import Protocol

from wse.feature.interfaces.icontent import GetContentProto
from wse.feature.interfaces.iobserver import AddObserverProto


class LoginFeatureProto(Protocol):
    """Protocol for Login container feature interface."""

    def clear_credential(self) -> None:
        """Clear the entered credential."""


class LoginProto(
    AddObserverProto,
    GetContentProto,
    LoginFeatureProto,
    Protocol,
):
    """Protocol for Login container interface."""


class LoginObserver(ABC):
    """ABC for observing Login container notifications."""

    @abstractmethod
    def success_authentication(self) -> None:
        """Notify about successful authentication."""
