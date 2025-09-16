"""Abstract base classes for Use Cases."""

from abc import ABC, abstractmethod
from typing import Generic

from injector import inject
from typing_extensions import override

from wse.data.repositories.abc import (
    AssignedTaskRepoABC,
    CalculationTaskRepoABC,
)
from wse.data.sources.assigned import AssignedSourceObserverABC
from wse.data.sources.user import UserObserverABC
from wse.feature.interfaces.types import ObserverT
from wse.feature.shared.schemas.exercise import Assigned

# Abstract base classes for Use Cases


class ObserverRegistryUseCaseABC(ABC, Generic[ObserverT]):
    """ABC for Use Case to register observer on event notifications."""

    @abstractmethod
    def add_observer(self, observer: ObserverT) -> None:
        """Add an observer on event notifications."""

    @abstractmethod
    def remove_observer(self, observer: ObserverT) -> None:
        """Remove an observer from event notifications."""


class GetQuestionUseCaseABC(ABC):
    """ABC for get exercise task question Use Case."""

    @abstractmethod
    def update(self) -> None:
        """Fetch task question."""


class CheckAnswerUseCaseABC(ABC):
    """ABC for check exercise user answer Use Case."""

    @abstractmethod
    def check(self, answer: str) -> None:
        """Check user answer."""


class GetSolutionUseCaseABC(ABC):
    """ABC for get current solution Use Case."""

    @abstractmethod
    def update_solution(self) -> None:
        """Set current solution to Data layer."""


# ABC for User Use Cases


class UserObserverRegistryUseCaseABC(
    ObserverRegistryUseCaseABC[UserObserverABC],
    ABC,
):
    """ABC for Use Case to register user event notifications."""

    @abstractmethod
    @override
    def add_observer(self, observer: UserObserverABC) -> None:
        """Register an observer on User event notifications."""

    @abstractmethod
    @override
    def remove_observer(self, observer: UserObserverABC) -> None:
        """Delete an observer from User event notifications."""


# ABC for Calculation exercise Use Cases


class _BaseCalculationUseCase:
    """Base calculation exercise Use Case."""

    @inject
    def __init__(self, repository: CalculationTaskRepoABC) -> None:
        """Construct the repository."""
        self._repository = repository


class GetCalculationQuestionUseCaseABC(
    _BaseCalculationUseCase,
    GetQuestionUseCaseABC,
    ABC,
):
    """ABC for get Calculation exercise task question Use Case."""


class CheckCalculationAnswerUseCaseABC(
    _BaseCalculationUseCase,
    CheckAnswerUseCaseABC,
    ABC,
):
    """ABC for get Calculation exercise user answer Use Case."""


class GetCalculationSolutionUseCaseABC(
    _BaseCalculationUseCase,
    GetSolutionUseCaseABC,
    ABC,
):
    """ABC for get Calculation correct solution Use Case."""


# ABC for Assigned exercise Use Cases


class AssignedObserverRegistryUseCaseABC(
    ObserverRegistryUseCaseABC[AssignedSourceObserverABC],
    ABC,
):
    """ABC for Assigned exercise source observer registry Use Case."""

    @abstractmethod
    def add_observer(self, observer: AssignedSourceObserverABC) -> None:
        """Register an observer to receive calculation task updates."""


class SetAssignedExerciseUseCaseABC(ABC):
    """ABC for set assigned exercise Ues Case."""

    @abstractmethod
    def set_exercise(self, exercise: Assigned) -> None:
        """Set assigned exercise."""


class _BaseAssignedTaskUseCase:
    """Base Assigned exercise task Use Case."""

    @inject
    def __init__(self, repository: AssignedTaskRepoABC) -> None:
        """Construct the repository."""
        self._repository = repository


class GetAssignedQuestionUseCaseABC(
    _BaseAssignedTaskUseCase,
    GetQuestionUseCaseABC,
    ABC,
):
    """ABC for get Assigned exercise task question Use Case."""


class CheckAssignedAnswerUseCaseABC(
    _BaseAssignedTaskUseCase,
    CheckAnswerUseCaseABC,
    ABC,
):
    """ABC for get Assigned exercise user answer Use Case."""


class GetAssignedSolutionUseCaseABC(
    _BaseAssignedTaskUseCase,
    GetSolutionUseCaseABC,
    ABC,
):
    """ABC for get Calculation correct solution feature."""
