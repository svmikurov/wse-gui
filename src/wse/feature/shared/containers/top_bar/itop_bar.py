"""Defines abc and protocols for the container interface."""

from abc import ABC, abstractmethod
from typing import Protocol

from typing_extensions import override

from wse.feature.base import Controller, ViewABC
from wse.feature.base.mixins import AddObserverMixin, NotifyNavigateMixin
from wse.feature.interfaces.icontent import GetContentProto
from wse.feature.interfaces.iobserver import AddObserverProto

# Top bar container


class TopBarContainerFeatureProto(Protocol):
    """Protocol for top bar container feature interface."""

    # API for container controller

    def update_balance(self, value: str) -> None:
        """Update balance."""


class TopBarContainerProto(
    AddObserverProto,
    GetContentProto,
    TopBarContainerFeatureProto,
    Protocol,
):
    """Protocol for top bar container interface."""


class TopBarContainerFeaturesABC(ABC):
    """Abstract base class for top bar container features."""

    # API for container controller

    @abstractmethod
    def update_balance(self, value: str) -> None:
        """Update balance."""


class TopBarContainerABC(
    TopBarContainerFeaturesABC,
    ViewABC,
    ABC,
):
    """Base class for Top Bar container."""


# Top bar controller


class TopBarControllerFeatureProto(Protocol):
    """Protocol for top bar controller features interface."""

    # API for view

    def update_balance(self, value: str) -> None:
        """Update balance."""


class TopBarControllerProto(
    TopBarControllerFeatureProto,
    AddObserverProto,
    GetContentProto,
    Protocol,
):
    """Protocol for Top Bar controller interface."""


class TopBarControllerFeaturesABC(ABC, TopBarControllerFeatureProto):
    """ABC for top bar controller features."""

    # Api for view

    @abstractmethod
    @override
    def update_balance(self, value: str) -> None:
        """Update balance."""


class TopBarControllerABC(
    AddObserverMixin,
    NotifyNavigateMixin,  # Container contains back button
    Controller,
    TopBarControllerFeaturesABC,
    ABC,
):
    """Base class for top bar controller."""


# Interface for pages where the container is injected


class TopBarViewMixinProto(Protocol):
    """Protocol for page view interface where top bar is injected."""

    def update_balance(self, value: str) -> None:
        """Update balance."""
