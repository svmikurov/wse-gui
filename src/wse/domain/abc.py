"""Abstract base classes for Use Cases."""

from abc import ABC, abstractmethod

from injector import inject

from wse.data.repositories import (
    CalculationRepositoryProto,
)


class _BaseUserCase:
    """Base calculation exercise Use Case."""

    @inject
    def __init__(self, repository: CalculationRepositoryProto) -> None:
        """Construct the repository."""
        self._repository = repository


class BaseGetQuestionUseCase(
    _BaseUserCase,
    ABC,
):
    """ABC for get calculation task question Use Case."""

    @abstractmethod
    def update(self) -> None:
        """Fetch task question."""


class BaseCheckCalculationUseCase(
    _BaseUserCase,
    ABC,
):
    """ABC for check calculation user answer Use Case."""

    @abstractmethod
    def check(self, answer: str) -> None:
        """Check user answer."""
