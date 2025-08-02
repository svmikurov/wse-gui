"""Defines abc and protocols for the container interface."""

from abc import ABC, abstractmethod
from typing import Protocol

from typing_extensions import override

from wse.config.layout import TopBarStyle, TopBarTheme
from wse.features.base import BaseController
from wse.features.base.container import NavigableContainerABC
from wse.features.base.mixins import AddObserverMixin, NotifyNavigateMixin
from wse.features.interfaces.icontainer import (
    IAddObserver,
    INavigableContainer,
)
from wse.features.interfaces.icontent import IGetContent

# Top bar container


class ITopBarContainerFeatures(Protocol):
    """Protocol for top bar container feature interface."""

    # API for container controller

    def update_balance(self, value: str) -> None:
        """Update balance."""


class ITopBarContainer(
    ITopBarContainerFeatures,
    INavigableContainer[TopBarStyle, TopBarTheme],
    Protocol,
):
    """Protocol for top bar container interface."""


class TopBarContainerFeaturesABC(ABC, ITopBarContainerFeatures):
    """Abstract base class for top bar container features."""

    # API for container controller

    @abstractmethod
    @override
    def update_balance(self, value: str) -> None:
        """Update balance."""


class BaseTopBarContainer(
    TopBarContainerFeaturesABC,
    NavigableContainerABC[TopBarStyle, TopBarTheme],
    ABC,
    ITopBarContainer,
):
    """Base class for Top Bar container."""


# Top bar controller


class ITopBarControllerFeatures(Protocol):
    """Protocol for top bar controller features interface."""

    # API for view

    def update_balance(self, value: str) -> None:
        """Update balance."""


class ITopBarController(
    ITopBarControllerFeatures,
    IAddObserver,
    IGetContent,
    Protocol,
):
    """Protocol for Top Bar controller interface."""


class TopBarControllerFeaturesABC(ABC, ITopBarControllerFeatures):
    """Abstract base class for top bar controller features."""

    # Api for view

    @abstractmethod
    @override
    def update_balance(self, value: str) -> None:
        """Update balance."""


class BaseTopBarController(
    AddObserverMixin,
    NotifyNavigateMixin,  # Container contains back button
    BaseController,
    TopBarControllerFeaturesABC,
    ABC,
    ITopBarController,
):
    """Base class for top bar controller."""


# Interface for pages where the container is injected


class ITopBarPageViewMixin(Protocol):
    """Protocol for page view interface where top bar is injected."""

    def update_balance(self, value: str) -> None:
        """Update balance."""
