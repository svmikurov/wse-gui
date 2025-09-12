"""User data source."""

from abc import ABC, abstractmethod
from dataclasses import replace
from typing import Literal

from typing_extensions import Unpack

from wse.data.entities.user import User, UserFieldType
from wse.data.sources.base.source import DataSourceGen

_NotifyT = Literal['balance_updated']


class UserSourceABC(ABC):
    """ABC for User source."""

    @abstractmethod
    def update_balance(self, balance: str) -> None:
        """Update balance."""


class UserObserverABC(ABC):
    """ABC for User source observer."""

    @abstractmethod
    def balance_updated(self, balance: str) -> None:
        """Handle the 'balance updated' event of User source."""


class UserSource(
    UserSourceABC,
    DataSourceGen[UserObserverABC, _NotifyT],
):
    """User data source."""

    def __init__(self) -> None:
        """Construct the source."""
        super().__init__()
        self._create_data()

    # API

    def update_balance(self, balance: str) -> None:
        """Update balance."""
        self._update_data(balance=balance)
        self.notify('balance_updated', balance=self._data.balance)
        print(f'Balance updated: {balance}')

    # Utility methods

    def _create_data(self) -> None:
        """Create entity data instance."""
        self._data = User()

    def _update_data(self, **new_data: Unpack[UserFieldType]) -> None:
        """Update entity data instance."""
        self._data = replace(self._data, **new_data)
