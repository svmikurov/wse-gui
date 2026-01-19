"""Abstract base class for Presentation domain."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from wse.data.dto import foreign as dto


class PresentationABC(ABC):
    """ABC for Presentations domain."""

    @abstractmethod
    def set_timeout(
        self,
        settings: dto.PresentationSettings,
    ) -> None:
        """Set presentation timeouts."""

    @abstractmethod
    async def wait_start_case_event(self) -> None:
        """Wait for start case event."""

    @abstractmethod
    async def wait_question_event(self) -> None:
        """Wait for question phase event."""

    @abstractmethod
    async def wait_answer_event(self) -> None:
        """Wait for answer phase event."""

    @abstractmethod
    async def wait_end_case_event(self) -> None:
        """Wait for end case event."""

    @abstractmethod
    async def get_progress(self) -> tuple[float, float]:
        """Get presentation progress value."""

    @abstractmethod
    def start(self) -> None:
        """Start presentation case."""

    @abstractmethod
    def pause(self) -> None:
        """Pause presentation."""

    @abstractmethod
    def unpause(self) -> None:
        """Unpause presentation."""

    @abstractmethod
    def stop(self) -> None:
        """Stop presentation."""

    @abstractmethod
    def complete_phase(self) -> None:
        """Complete the current phase."""
