"""Abstract base classes for Use Cases."""

from abc import ABC, abstractmethod

from injector import inject
from typing_extensions import override

from wse.data.repositories import (
    CalculationRepositoryProto,
)

from . import (
    CheckCalculationUseCaseProto,
    GetQuestionUseCaseProto,
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
    GetQuestionUseCaseProto,
):
    """ABC for get calculation task question Use Case."""

    @abstractmethod
    @override
    def fetch(self) -> None:
        """Fetch task question."""


class BaseCheckCalculationUseCase(
    _BaseUserCase,
    ABC,
    CheckCalculationUseCaseProto,
):
    """ABC for check calculation user answer Use Case."""

    @abstractmethod
    @override
    def check(self, answer: str) -> None:
        """Check user answer."""
