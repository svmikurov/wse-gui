"""Abstract base classes for Home screen UI layer."""

from abc import ABC, abstractmethod
from typing import Literal

from wse.apps.nav_id import NavID
from wse.feature.base import ViewABC
from wse.feature.base.mixins import AddObserverGenT

_NotifyT = Literal[
    'user_authenticated',
    'user_anonymous',
]

# ViewModel


class HomeViewModelObserverABC(ABC):
    """ABC for Home ViewModel observer."""

    @abstractmethod
    def user_authenticated(self) -> None:
        """Set content for authenticated user."""

    @abstractmethod
    def user_anonymous(self) -> None:
        """Set content for anonymous user."""


class HomeViewModelABC(
    AddObserverGenT[HomeViewModelObserverABC, _NotifyT],
    ABC,
):
    """ABC for Home screen ViewModel."""

    @abstractmethod
    def update_context(self) -> None:
        """Update screen context."""

    @abstractmethod
    def navigate(self, nav_id: NavID) -> None:
        """Handle the navigate event, callback."""


# View


class HomeViewABC(
    HomeViewModelObserverABC,
    ViewABC,
    ABC,
):
    """ABC for Home screen View."""
