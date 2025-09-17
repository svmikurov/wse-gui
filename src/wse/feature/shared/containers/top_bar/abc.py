"""Abstract base class for TopBar."""

from abc import ABC, abstractmethod

from wse.feature.base import Controller
from wse.feature.base.mixins import AddObserverMixin, NotifyNavigateMixin
from wse.ui.base.abc import ViewABC


class TopBarControllerFeaturesABC(ABC):
    """ABC for top bar controller features.

    Provides API for View.
    """

    @abstractmethod
    def update_balance(self, value: str) -> None:
        """Update balance."""


class TopBarContainerFeaturesABC(ABC):
    """Abstract base class for top bar container features.

    Provides API for View.
    """

    @abstractmethod
    def update_balance(self, value: str) -> None:
        """Update balance."""


class TopBarContainerABC(
    TopBarContainerFeaturesABC,
    ViewABC,
    ABC,
):
    """Base class for Top Bar container."""


class TopBarControllerABC(
    AddObserverMixin,
    NotifyNavigateMixin,  # Container contains back button
    Controller,
    TopBarControllerFeaturesABC,
    ABC,
):
    """Base class for top bar controller."""
