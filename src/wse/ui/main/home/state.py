"""Home screen state."""

import logging
from dataclasses import dataclass, replace
from typing import TypedDict

from injector import inject
from typing_extensions import Unpack, override

from wse.apps.nav_id import NavID
from wse.core.interfaces import Navigable
from wse.data.repositories.abc import HomeRepoABC

from .abc import HomeViewModelABC

logger = logging.getLogger(__name__)


class _DataFieldType(TypedDict, total=False):
    """Field types for UI state data."""

    is_authenticated: bool


@dataclass(frozen=True)
class HomeUIState:
    """Home screen UI state data."""

    is_authenticated: bool = False


@inject
@dataclass
class HomeViewModel(
    HomeViewModelABC,
):
    """Home screen ViewModel."""

    _navigator: Navigable

    _home_repo: HomeRepoABC

    def __post_init__(self) -> None:
        """Construct the model."""
        self._create_data()

    # API

    @override
    def update_context(self) -> None:
        """Update screen context."""
        self._set_auth_state()

    # TODO: Move to base class.
    @override
    def navigate(self, nav_id: NavID) -> None:
        """Handle the navigate event, callback."""
        self._navigator.navigate(nav_id=nav_id)

    # Utility methods

    def _create_data(self) -> None:
        """Create UI state data."""
        self._data = HomeUIState()

    def _update_data(self, **data: Unpack[_DataFieldType]) -> None:
        """Update UI state data."""
        replace(self._data, **data)

    def _set_auth_state(self) -> None:
        """Set user authenticated state."""
        if is_authenticated := self._home_repo.is_authenticated:
            self._notify('user_authenticated')
        else:
            self._notify('user_anonymous')

        self._update_data(is_authenticated=is_authenticated)
