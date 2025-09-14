"""Abstract base classes."""

from abc import ABC, abstractmethod

from wse.core.navigation.nav_id import NavID


class NavigateABC(ABC):
    """ABC for navigate feature."""

    @abstractmethod
    def navigate(self, nav_id: NavID) -> None:
        """Handle the navigate event."""
