"""Abstract base class for time control."""

from abc import ABC, abstractmethod


class TimerABC(ABC):
    """ABC for time control."""

    @abstractmethod
    async def start(self, timeout: int | None = None) -> None:
        """Start event timer."""

    @abstractmethod
    def is_timer(self) -> bool:
        """Is the timer started."""

    @abstractmethod
    def cancel(self) -> None:
        """Cancel event timer."""

    @abstractmethod
    def on_pause(self) -> None:
        """Pause the event."""

    @abstractmethod
    def is_pause(self) -> bool:
        """Is the event paused."""

    @abstractmethod
    def unpause(self) -> None:
        """Unpause the event."""
