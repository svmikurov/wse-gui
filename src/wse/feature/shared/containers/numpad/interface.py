"""Abstract base classes for numpad components and numpad observer."""

from abc import ABC, abstractmethod

from .protocols import NumpadObserverProto


class NumpadObserver(ABC, NumpadObserverProto):
    """Abstract base class for numpad observer."""

    @abstractmethod
    def numpad_entered(self, value: str) -> None:
        """Notification about updating the entered value."""
