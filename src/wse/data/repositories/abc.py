"""Abstract base class for repository."""

from abc import ABC, abstractmethod

from typing_extensions import override

from . import CalculationRepositoryProto


class BaseCalculationRepository(
    ABC,
    CalculationRepositoryProto,
):
    """Abstract base class for calculation repository."""

    @abstractmethod
    @override
    def fetch_task(self) -> None:
        """Fetch calculation exercise task question."""

    @abstractmethod
    @override
    def check_answer(self, answer: str) -> None:
        """Check calculation exercise task user answer."""
