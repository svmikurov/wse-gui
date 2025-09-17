"""Assigned exercise Use Cases."""

import logging

from injector import inject
from typing_extensions import override

from wse.data.sources.assigned import (
    AssignedExerciseSource,
)

from ..data.repositories.abc import AssignedTaskRepoABC
from ..data.repositories.assigned_task import AssignedTaskRepo
from ..data.sources.task import ResultObserverABC, TaskObserverABC
from ..feature.shared.schemas.exercise import Assigned
from .abc import SubscribeUseCaseABC
from .abc.assigned import (
    CheckAssignedAnswerUseCaseABC,
    GetAssignedQuestionUseCaseABC,
    GetAssignedSolutionUseCaseABC,
    SetAssignedExerciseUseCaseABC,
)

logger = logging.getLogger(__name__)

# Exercise


class _AssignedExercise:
    """Base Assigned exercise."""

    @inject
    def __init__(self, source: AssignedExerciseSource) -> None:
        """Construct the registry."""
        self._source = source


class SetAssignedExerciseUseCase(
    _AssignedExercise,
    SetAssignedExerciseUseCaseABC,
):
    """Set assigned exercise Ues Case."""

    def set_exercise(self, exercise: Assigned) -> None:
        """Set assigned exercise."""
        self._source.set_exercise(exercise)


# Observer


class AssignedObserverRegistryUseCase(
    SubscribeUseCaseABC[TaskObserverABC],
):
    """Assigned exercise source observer registry the Use Case."""

    @inject
    def __init__(self, repository: AssignedTaskRepoABC) -> None:
        """Construct the case."""
        self._repository = repository

    def add_listener(self, observer: TaskObserverABC) -> None:
        """Register an observer to receive calculation task updates."""
        self._repository.add_observer(observer)

    def remove_listener(self, observer: TaskObserverABC) -> None:
        """Remove an observer from event notifications."""
        self._repository.remove_observer(observer)


# Task question/answer


class GetAssignedQuestionUseCase(GetAssignedQuestionUseCaseABC):
    """Get Assigned exercise task question the Use Case."""

    @override
    def update(self) -> None:
        """Fetch task question."""
        self._repository.fetch_task()


class CheckAssignedAnswerUseCase(CheckAssignedAnswerUseCaseABC):
    """Check Assigned exercise task user answer the Use Case."""

    @override
    def check(self, answer: str) -> None:
        """Check user answer."""
        self._repository.fetch_result(answer)


class GetAssignedSolutionUseCase(GetAssignedSolutionUseCaseABC):
    """Get Assigned correct solution Use Case."""

    @override
    def update_solution(self) -> None:
        """Set current solution to Data layer."""
        self._repository.update_solution()


# Business logic


class AssignedLogicUseCase(ResultObserverABC):
    """Assigned exercise logic Use Case."""

    @inject
    def __init__(
        self,
        repository: AssignedTaskRepo,
    ) -> None:
        """Construct the case."""
        self._repository = repository
        self._repository.add_observer(self)

    def result_updated(self, is_correct: bool) -> None:
        """Handle the answer check result."""
        if is_correct:
            self._repository.fetch_task()
        else:
            self._repository.update_solution()
