"""Abstract Base Classes for observe."""

from abc import ABC, abstractmethod
from typing import Generic

from wse.feature.interfaces.types import ListenerT


class SubscribeUseCaseABC(ABC, Generic[ListenerT]):
    """ABC for Use Case to subscribe observer on event notifications."""

    @abstractmethod
    def add_listener(self, observer: ListenerT) -> None:
        """Add a new listener to this data source."""

    @abstractmethod
    def remove_listener(self, observer: ListenerT) -> None:
        """Remove a listener from this data source."""
