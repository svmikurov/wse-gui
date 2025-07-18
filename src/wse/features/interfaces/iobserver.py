"""Defines protocols for interface of Observer pattern components."""

from typing import Protocol


class IObserver(
    Protocol,
):
    """Protocol for observer interface of Observer pattern."""


class ISubject(
    Protocol,
):
    """Protocol for subject interface of Observer pattern."""

    def notify(self, notification: str, **kwargs: object) -> None:
        """Notify all observers an event has occurred."""

    @property
    def observers(self) -> list[IObserver]:
        """Get observers."""

    # This method duplicates the `IAddObserver` mixin `add_observer`
    # method from `.icontainer.` module to avoid circular imports in
    # multiple inheritance.
    def add_observer(self, observer: IObserver) -> None:
        """Add a new observer to this subject."""
