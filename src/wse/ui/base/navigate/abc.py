"""Abstract Base Classes for navigation."""

from abc import ABC, abstractmethod

from wse.core.navigation import NavID


class NavigateABC(ABC):
    """ABC for navigate feature."""

    @abstractmethod
    def navigate(self, nav_id: NavID) -> None:
        """Handle the navigate event."""

# TODO: Move to .view module?
class OnOpenABC(ABC):
    """ABC for open screen event."""

    @abstractmethod
    def on_open(self) -> None:
        """Call methods on screen open event."""


# TODO: Move to .view module?
class OnCloseABC(ABC):
    """ABC for close screen event."""

    @abstractmethod
    def on_close(self) -> None:
        """Call methods before close the screen."""
