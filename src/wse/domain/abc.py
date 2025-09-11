"""Abstract base classes for Use Cases."""

from abc import ABC, abstractmethod

from injector import inject

from wse.data.repositories.protocol import CalculationRepoProto


class _BaseUserCase:
    """Base calculation exercise Use Case."""

    @inject
    def __init__(self, repository: CalculationRepoProto) -> None:
        """Construct the repository."""
        self._repository = repository


class GetQuestionUseCaseABC(
    _BaseUserCase,
    ABC,
):
    """ABC for get calculation task question Use Case."""

    @abstractmethod
    def update(self) -> None:
        """Fetch task question."""


class CheckCalculationUseCaseABC(
    _BaseUserCase,
    ABC,
):
    """ABC for check calculation user answer Use Case."""

    @abstractmethod
    def check(self, answer: str) -> None:
        """Check user answer."""
