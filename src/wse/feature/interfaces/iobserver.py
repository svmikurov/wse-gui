"""Defines protocols for interface of Observer pattern components."""

from typing import Protocol, TypeVar

NotifyT_co = TypeVar('NotifyT_co', covariant=True)
NotifyT_contra = TypeVar('NotifyT_contra', contravariant=True)


class ObserverProto(
    Protocol,
):
    """Protocol for observer interface of Observer pattern."""


class Observable(
    Protocol,
):
    """Protocol for subject interface of Observer pattern."""

    def notify(self, notification: NotifyT_contra, **kwargs: object) -> None:
        """Notify all observers an event has occurred."""

    @property
    def observers(self) -> list[ObserverProto]:
        """Get observers."""

    # This method duplicates the `IAddObserver` mixin `add_observer`
    # method from `.icontainer.` module to avoid circular imports in
    # multiple inheritance.
    def add_observer(self, observer: ObserverProto) -> None:
        """Add a new observer to this subject."""


class AddObserverProto(Protocol):
    """Protocol for observer subscription capability interface."""

    _subject: Observable

    def add_observer(self, observer: ObserverProto) -> None:
        """Subscribe observer an event has occurred."""
