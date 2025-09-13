"""Abstract base class for repository."""

from abc import ABC, abstractmethod


class CalculationRepoABC(ABC):
    """Abstract base class for calculation repository."""

    @abstractmethod
    def fetch_task(self) -> None:
        """Fetch calculation exercise task question."""

    @abstractmethod
    def fetch_result(self, answer: str) -> None:
        """Fetch user answer check result."""
