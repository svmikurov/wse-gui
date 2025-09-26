"""Defines abc and protocols for the container interface."""

from abc import ABC, abstractmethod

from wse.ui.base.content.abc import GetContentABC

# Top bar container


class TopBarContainerFeatureABC(ABC):
    """ABC for top bar container feature interface."""

    # API for container controller

    @abstractmethod
    def update_balance(self, value: str) -> None:
        """Update balance."""


class TopBarContainerABC(
    GetContentABC,
    TopBarContainerFeatureABC,
):
    """ABC for top bar container interface."""


# Top bar controller


class TopBarControllerFeatureABC(ABC):
    """Protocol for top bar controller features interface."""

    # API for view

    @abstractmethod
    def update_balance(self, value: str) -> None:
        """Update balance."""


class TopBarControllerProto(
    TopBarControllerFeatureABC,
    GetContentABC,
    ABC,
):
    """ABC for Top Bar controller interface."""


# Interface for pages where the container is injected


class TopBarViewMixinABC(ABC):
    """ABC for page view interface where top bar is injected."""

    @abstractmethod
    def update_balance(self, value: str) -> None:
        """Update balance."""
