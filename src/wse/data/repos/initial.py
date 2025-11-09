"""App initial data repository."""

from abc import ABC, abstractmethod
from dataclasses import dataclass

from injector import inject
from typing_extensions import override

from wse.data.sources.user import UserSource
from wse.data.sources.user_network import UserNetworkSource


class InitialDataRepoABC(ABC):
    """ABC for initial data repository."""

    @abstractmethod
    def update_data(self) -> None:
        """Update app initial data."""


@inject
@dataclass
class InitialDataRepo(InitialDataRepoABC):
    """Initial data repository."""

    # TODO: Update to depend on abstraction
    _user_local_source: UserSource
    _user_network_source: UserNetworkSource

    @override
    def update_data(self) -> None:
        """Update app initial data."""
        if data := self._user_network_source.fetch_data():
            if balance := data.balance:
                self._user_local_source.update_balance(balance=balance)
