"""Abstract base class for Account UI layer components."""

from abc import ABC, abstractmethod
from typing import Literal

import toga

from wse.core.navigation.nav_id import NavID
from wse.feature.observer.mixins import SubjectGen
from wse.ui.base.navigate import NavigateABC, OnCloseABC
from wse.ui.base.view.abc import ViewABC

_NotifyT = Literal[
    'user_authenticated',
    'user_anonymous',
]

# ViewModel


# TODO: Move to base mixin
class ViewModelObserverABC(ABC):
    """ABC for ViewModel observer."""

    @abstractmethod
    def user_authenticated(self) -> None:
        """Set content for authenticated user."""

    @abstractmethod
    def user_anonymous(self) -> None:
        """Set content for anonymous user."""


# TODO: Move to mixin
class ViewModelFeatureABC(ABC):
    """ABC for ViewModel feature."""

    @abstractmethod
    def refresh_context(self) -> None:
        """Refresh screen context."""

    @abstractmethod
    def navigate(self, nav_id: NavID) -> None:
        """Handle the navigate event, callback."""


class AuthViewModelABC(
    SubjectGen[ViewModelObserverABC, _NotifyT],
    NavigateABC,
    OnCloseABC,
    ABC,
):
    """ABC for Auth ViewModel."""

    @abstractmethod
    def refresh_context(self) -> None:
        """Refresh screen context."""

    @abstractmethod
    def navigate(self, nav_id: NavID) -> None:
        """Handle the navigate event, callback."""

    # Callback methods

    @abstractmethod
    def logout(self, _: toga.Button) -> None:
        """Logout, button callback method."""

    # Feature

    @abstractmethod
    def handle_success_authentication(self) -> None:
        """Handle the success authentication."""


# View


class AuthViewABC(
    ViewModelObserverABC,
    ViewABC,
    OnCloseABC,
    ABC,
):
    """ABC for Auth View."""
