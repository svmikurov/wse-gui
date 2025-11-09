"""Abstract Base Classes for Assigned exercise Use Cases."""

from abc import ABC, abstractmethod

from injector import inject

from wse.api.schemas.exercise import Assigned
from wse.data.repos.abc import AssignedTaskRepoABC
from wse.data.sources.assigned import AssignedSourceObserverABC
from wse.domain.abc import SubscribeUseCaseABC
from wse.domain.abc.task import (
    CheckAnswerUseCaseABC,
    GetQuestionUseCaseABC,
    GetSolutionUseCaseABC,
)


class SubscribeAssignedUseCaseABC(
    SubscribeUseCaseABC[AssignedSourceObserverABC],
    ABC,
):
    """ABC for Assigned exercise source observer registry Use Case."""

    @abstractmethod
    def add_listener(self, observer: AssignedSourceObserverABC) -> None:
        """Register an observer to receive calculation task updates."""

    @abstractmethod
    def remove_listener(self, observer: AssignedSourceObserverABC) -> None:
        """Remove a listener from this data source."""


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
