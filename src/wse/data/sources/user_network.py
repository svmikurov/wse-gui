"""User data Network source."""

from abc import ABC, abstractmethod

from injector import inject

from wse.core.api.data import DataApiABC
from wse.feature.api.schemas.core import InitialData


class UserNetworkSourceABC(ABC):
    """ABC for User Network data source."""

    @abstractmethod
    def fetch_data(self) -> InitialData | None:
        """Fetch app initial data."""


class UserNetworkSource(UserNetworkSourceABC):
    """User data Network source."""

    @inject
    def __init__(self, api_client: DataApiABC) -> None:
        """Construct the source."""
        self._api_client = api_client

    def fetch_data(self) -> InitialData | None:
        """Fetch app initial data."""
        if response_data := self._api_client.fetch_initial_data():
            return response_data.data
        return None
