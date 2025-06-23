"""Defines protocols for interface of Observer pattern components."""

from typing import Protocol


class IObserver(
    Protocol,
):
    """Protocol for observer interface of Observer pattern."""


class IAddObserver(Protocol):
    """Protocol for add observer interface."""

    def add_observer(self, observer: IObserver) -> None:
        """Add a new observer to this subject."""


class ISubject(
    IAddObserver,
    Protocol,
):
    """Protocol for subject interface of Observer pattern."""

    def notify(self, notification: str, **kwargs: object) -> None:
        """Notify all observers an event has occurred."""
