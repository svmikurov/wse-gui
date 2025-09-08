"""Abstract base class for repository."""

from abc import ABC, abstractmethod


class BaseCalculationRepository(ABC):
    """Abstract base class for calculation repository."""

    @abstractmethod
    def fetch_task(self) -> None:
        """Fetch calculation exercise task question."""

    @abstractmethod
    def check_answer(self, answer: str) -> None:
        """Check calculation exercise task user answer."""
