"""Abstract base class for TopBar."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Literal

from wse.feature.observer.generic import SubjectGenABC
from wse.feature.observer.mixins import (
    NotifyNavigateMixin,
    ObserverManager,
)
from wse.ui.base.content.abc import GetContentABC
from wse.ui.base.navigate import NavigateABC
from wse.ui.base.view.abc import ViewABC

NotifyT = Literal['navigate']


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


@dataclass
class TopBarContainerABC(
    GetContentABC,
    SubjectGenABC[NavigateABC, NotifyT],
    TopBarContainerFeaturesABC,
    ViewABC,
    ABC,
):
    """Base class for Top Bar container."""


@dataclass
class TopBarControllerABC(
    GetContentABC,
    ObserverManager,
    NotifyNavigateMixin,  # Container contains back button
    NavigateABC,
    TopBarControllerFeaturesABC,
    ABC,
):
    """Base class for top bar controller."""
