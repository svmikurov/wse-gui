"""User data source."""

import logging
from abc import ABC, abstractmethod
from dataclasses import replace
from typing import Literal

from typing_extensions import Unpack

from wse.data.entities.user import User, UserFieldType
from wse.data.sources.base.source import SourceGen

_NotifyT = Literal['balance_updated']

logger = logging.getLogger(__name__)


class UserSourceABC(ABC):
    """ABC for User source."""

    @abstractmethod
    def update_balance(self, balance: str) -> None:
        """Update balance with listeners notify."""


class UserObserverABC(ABC):
    """ABC for User source observer."""

    @abstractmethod
    def balance_updated(self, balance: str) -> None:
        """Handle the 'balance updated' event of User source."""


class UserSource(
    UserSourceABC,
    SourceGen[UserObserverABC, _NotifyT],
):
    """User data source."""

    def __init__(self) -> None:
        """Construct the source."""
        super().__init__()
        self._create_data()

    def add_listener(self, listener: UserObserverABC) -> None:  # type: ignore[override]
        """Notify new listener about state of user data."""
        super().add_listener(listener)
        if self._data.balance:
            listener.balance_updated(balance=self._data.balance)

    # API

    def update_balance(self, balance: str) -> None:
        """Update balance with listeners notify."""
        self._update_data(balance=balance)
        self.notify('balance_updated', balance=self._data.balance)

    # Utility methods

    def _create_data(self) -> None:
        """Create entity data instance."""
        self._data = User()

    def _update_data(self, **new_data: Unpack[UserFieldType]) -> None:
        """Update entity data instance."""
        self._data = replace(self._data, **new_data)
