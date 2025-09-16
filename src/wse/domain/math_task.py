"""Calculation task Use Cases."""

import logging

from injector import inject
from typing_extensions import override

from ..data.repositories.abc import CalculationTaskRepoABC
from ..data.sources.task import (
    TaskObserverABC,
)
from .abc import (
    CheckCalculationAnswerUseCaseABC,
    GetCalculationQuestionUseCaseABC,
    GetCalculationSolutionUseCaseABC,
)

logger = logging.getLogger(__name__)


class CalculationObserverRegistryUseCase:
    """Use Case for subscribing to calculation task events."""

    @inject
    def __init__(self, repository: CalculationTaskRepoABC) -> None:
        """Construct the case."""
        self._repository = repository

    def register_observer(self, observer: TaskObserverABC) -> None:
        """Register an observer to receive calculation task updates."""
        self._repository.add_observer(observer)

    def remove_observer(self, observer: TaskObserverABC) -> None:
        """Remove observer from subject observers."""
        self._repository.remove_observer(observer)


class GetCalculationQuestionUseCase(GetCalculationQuestionUseCaseABC):
    """Fetch calculation exercise task question Use Case."""

    @inject
    def __init__(
        self,
        repository: CalculationTaskRepoABC,
    ) -> None:
        """Construct the case."""
        super().__init__(repository)

    @override
    def update(self) -> None:
        """Get task question."""
        self._repository.fetch_task()


class CheckCalculationAnswerUseCase(CheckCalculationAnswerUseCaseABC):
    """Check calculation exercise user task answer Use Case."""

    @override
    def check(self, answer: str) -> None:
        """Check user answer."""
        self._repository.fetch_result(answer)


class GetCalculationSolutionUseCase(GetCalculationSolutionUseCaseABC):
    """Get Calculation correct solution Use Case."""

    @override
    def update_solution(self) -> None:
        """Set current solution to Data layer."""
        self._repository.update_solution()
