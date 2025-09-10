"""Protocols for Use Cases."""

from typing import Protocol


class UpdateQuestionUseCaseProto(Protocol):
    """Protocol for get task question Use Case interface."""

    def update(self) -> None:
        """Fetch task."""


class CheckCalculationUseCaseProto(Protocol):
    """Protocol for check user answer Use Case interface."""

    def check(self, answer: str) -> None:
        """Check user answer."""
