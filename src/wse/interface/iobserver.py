"""Defines protocol interfaces for Observer pattern."""

from typing import Protocol

from toga.sources import Listener

# ruff: noqa: D101, D102, D204, E301, E302
# fmt: off


class ISubject(Protocol):
    """An observable object in the Observer pattern."""
    def add_listener(self, listener: object) -> None:
        """Register an observer to receive notifications."""
    def notify(self, notification: str, **kwargs: object) -> None:
        """Register an observer to receive notifications."""

class IListener(Listener, Protocol):
    """Protocol defining the interface for subject listener."""
