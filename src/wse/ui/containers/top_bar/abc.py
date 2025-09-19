"""Abstract base class for TopBar."""

from abc import ABC, abstractmethod
from typing import Literal

from wse.feature.base import Controller
from wse.feature.base.mixins import (
    AddObserverGenT,
    AddObserverMixin,
    NotifyNavigateMixin,
)
from wse.ui.base.abc.navigate import NavigateABC
from wse.ui.base.abc.view import ViewABC


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


_NotifyT = Literal['navigate']


class TopBarContainerABC(
    AddObserverGenT[NavigateABC, _NotifyT],
    TopBarContainerFeaturesABC,
    ViewABC,
    ABC,
):
    """Base class for Top Bar container."""


class TopBarControllerABC(
    AddObserverMixin,
    NotifyNavigateMixin,  # Container contains back button
    Controller,
    NavigateABC,
    TopBarControllerFeaturesABC,
    ABC,
):
    """Base class for top bar controller."""
