"""Abstract base classes for numpad components and numpad observer."""

from abc import ABC, abstractmethod


class NumpadObserverABC(ABC):
    """Abstract base class for numpad observer."""

    @abstractmethod
    def numpad_entered(self, value: str) -> None:
        """Notification about updating the entered value."""
