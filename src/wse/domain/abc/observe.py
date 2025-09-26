"""Abstract Base Classes for listener."""

from abc import ABC, abstractmethod
from typing import Generic

from wse.types import ListenerT


class SubscribeUseCaseABC(ABC, Generic[ListenerT]):
    """ABC for Use Case to subscribe listener on event notifications."""

    @abstractmethod
    def add_listener(self, listener: ListenerT) -> None:
        """Add a new listener to this data source."""

    @abstractmethod
    def remove_listener(self, listener: ListenerT) -> None:
        """Remove a listener from this data source."""
