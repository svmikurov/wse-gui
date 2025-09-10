"""Protocols for repository interfaces."""

from typing import Protocol


class CalculationRepositoryProto(Protocol):
    """Protocol for calculation repository interface."""

    def fetch_task(self) -> None:
        """Fetch calculation exercise task question."""

    def fetch_result(self, answer: str) -> None:
        """Check calculation exercise task user answer."""
