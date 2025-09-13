"""Abstract base classes for Use Cases."""

from abc import ABC, abstractmethod

from injector import inject

from wse.data.repositories.protocol import CalculationRepoProto
from wse.data.sources.user import UserObserverABC

# User (auth) Use Cases


class UserObserverRegistryUseCaseABC(ABC):
    """ABC for Use Case to register user event notifications."""

    @abstractmethod
    def register_observer(self, observer: UserObserverABC) -> None:
        """Register an observer to receive calculation task updates."""


# Calculation Use Cases


class _BaseCalculationUseCase:
    """Base calculation exercise Use Case."""

    @inject
    def __init__(self, repository: CalculationRepoProto) -> None:
        """Construct the repository."""
        self._repository = repository


class GetQuestionUseCaseABC(
    _BaseCalculationUseCase,
    ABC,
):
    """ABC for get calculation task question Use Case."""

    @abstractmethod
    def update(self) -> None:
        """Fetch task question."""


class CheckCalculationUseCaseABC(
    _BaseCalculationUseCase,
    ABC,
):
    """ABC for check calculation user answer Use Case."""

    @abstractmethod
    def check(self, answer: str) -> None:
        """Check user answer."""
