"""Abstract Base Classes protocols for Observer pattern components."""

from abc import ABC, abstractmethod
from typing import override

from .generic import NotifyGenABC, ObserverManagerGenABC


class ObserverManagerABC(ObserverManagerGenABC[object], ABC):
    """ABC for observer adding."""

    @property
    @override
    @abstractmethod
    def observers(self) -> list[object]:
        """Get observers."""

    @abstractmethod
    @override
    def add_observer(self, observer: object) -> None:
        """Add a new observer to this subject."""

    @abstractmethod
    @override
    def remove_observer(self, observer: object) -> None:
        """Remove an observer from this subject."""


class NotifyABC(NotifyGenABC[str], ABC):
    """ABC for observer notification."""

    @abstractmethod
    @override
    def notify(self, notification: str, **kwargs: object) -> None:
        """Notify all observers an event has occurred."""


class SubjectABC(
    ObserverManagerABC,
    NotifyABC,
    ABC,
):
    """ABC for Subject of Observer pattern."""
