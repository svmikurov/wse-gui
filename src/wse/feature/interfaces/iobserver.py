"""Defines protocols for interface of Observer pattern components."""

from abc import ABC, abstractmethod
from typing import Protocol, TypeVar

NotifyT_co = TypeVar('NotifyT_co', covariant=True)
NotifyT_contra = TypeVar('NotifyT_contra', contravariant=True)


class ObserverProto(
    Protocol,
):
    """Protocol for observer interface of Observer pattern."""


class SubjectABC(ABC):
    """Protocol for subject interface of Observer pattern."""

    @abstractmethod
    def notify(self, notification: str, **kwargs: object) -> None:
        """Notify all observers an event has occurred."""

    @property
    @abstractmethod
    def observers(self) -> list[ObserverProto]:
        """Get observers."""

    # This method duplicates the `IAddObserver` mixin `add_observer`
    # method from `.icontainer.` module to avoid circular imports in
    # multiple inheritance.
    @abstractmethod
    def add_observer(self, observer: ObserverProto) -> None:
        """Add a new observer to this subject."""

    @abstractmethod
    def remove_observer(self, observer: ObserverProto) -> None:
        """Remove an observer from this subject."""


class AddObserverProto(Protocol):
    """Protocol for observer subscription capability interface."""

    _subject: SubjectABC

    def add_observer(self, observer: ObserverProto) -> None:
        """Subscribe observer an event has occurred."""

    def remove_observer(self, observer: ObserverProto) -> None:
        """Remove observer from notifications."""
