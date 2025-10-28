"""Generic Abstract Base Classes for Observer pattern.

Contains base classes for:
    - Subject:
        * observer management (methods: `add_observer`,
          `remove_observer`, `observers`)
        * observer notification (method: `notify`)
    - Observer:
        * observer methods (`methods: update`, ...)
"""

from abc import ABC, abstractmethod
from typing import Generic

from wse.types import NotifyT, ObserverT

# Subject


class NotifyGenABC(ABC, Generic[NotifyT]):
    """ABC for observer notification."""

    @abstractmethod
    def notify(self, notification: NotifyT, **kwargs: object) -> None:
        """Notify all observers an event has occurred."""


class ObserverManagerGenABC(ABC, Generic[ObserverT]):
    """ABC for observer management."""

    @property
    @abstractmethod
    def observers(self) -> list[ObserverT]:
        """Get observers."""

    @abstractmethod
    def add_observer(self, observer: ObserverT) -> None:
        """Add a new observer to this subject."""

    @abstractmethod
    def remove_observer(self, observer: ObserverT) -> None:
        """Remove an observer from this subject."""


class SubjectGenABC(
    ObserverManagerGenABC[ObserverT],
    NotifyGenABC[NotifyT],
    Generic[ObserverT, NotifyT],
):
    """ABC for Subject observer."""
