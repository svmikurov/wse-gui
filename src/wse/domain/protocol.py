"""Protocols for Use Cases."""

from typing import Protocol


class GetQuestionUseCaseProto(Protocol):
    """Protocol for get task question Use Case interface."""

    def fetch(self) -> None:
        """Fetch task."""


class CheckCalculationUseCaseProto(Protocol):
    """Protocol for check user answer Use Case interface."""

    def check(self, answer: str) -> None:
        """Check user answer."""
