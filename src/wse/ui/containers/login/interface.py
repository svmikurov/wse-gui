"""Login controller interface.

Use ``LoginFeatureInterface`` to invoke a feature of Login container.

Use ``LoginObserverABC`` to define methods for listing Login container
notifications.
"""

from abc import ABC, abstractmethod

from wse.ui.base.content.abc import GetContentABC


class LoginFeatureABC(ABC):
    """ABC for Login container feature interface."""

    @abstractmethod
    def clear_credential(self) -> None:
        """Clear the entered credential."""


class LoginABC(
    GetContentABC,
    LoginFeatureABC,
):
    """ABC for Login container interface."""


class LoginObserver(ABC):
    """ABC for observing Login container notifications."""

    @abstractmethod
    def success_authentication(self) -> None:
        """Notify about successful authentication."""
