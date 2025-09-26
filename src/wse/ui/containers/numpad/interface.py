"""Abstract base classes for numpad components and numpad observer."""

from abc import ABC, abstractmethod
from typing import Literal

NumPadNotifyT = Literal['numpad_entered']


class NumPadObserverABC(ABC):
    """Abstract base class for numpad observer."""

    @abstractmethod
    def numpad_entered(self, value: str) -> None:
        """Notification about updating the entered value."""
