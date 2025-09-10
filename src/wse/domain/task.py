"""Task Use Cases."""

from injector import inject
from typing_extensions import override

from ..data.repositories import CalculationRepositoryProto
from ..data.repositories.calculation_task import CalculationTaskRepository
from ..data.sources.task import (
    TaskSourceObserveABC,
    TaskSourceResultObserveABC,
)
from .abc import (
    BaseCheckCalculationUseCase,
    BaseGetQuestionUseCase,
)


class SubscribeExerciseSourceUseCase:
    """Proxy Use Case to subscribe for Calculation source events."""

    @inject
    def __init__(self, repository: CalculationTaskRepository) -> None:
        """Construct the case."""
        self._repository = repository

    def subscribe(self, listener: TaskSourceObserveABC) -> None:
        """Add listener."""
        self._repository.throw_listener(listener)


class UpdateQuestionUseCase(
    BaseGetQuestionUseCase,
):
    """Fetch calculation exercise task question Use Case."""

    @inject
    def __init__(
        self,
        repository: CalculationRepositoryProto,
    ) -> None:
        """Construct the case."""
        super().__init__(repository)

    @override
    def update(self) -> None:
        """Get task question."""
        self._repository.fetch_task()


class CheckCalculationUseCase(
    BaseCheckCalculationUseCase,
):
    """Check calculation exercise user task answer Use Case."""

    @override
    def check(self, answer: str) -> None:
        """Check user answer."""
        self._repository.fetch_result(answer)


class CalculationLogicUseCase(TaskSourceResultObserveABC):
    """Calculation exercise logic."""

    @inject
    def __init__(
        self,
        repository: CalculationTaskRepository,
    ) -> None:
        """Construct the case."""
        self._repository = repository
        self._repository.throw_listener(self)

    def result_updated(self, is_correct: bool) -> None:
        """Handle the answer check result."""
        if is_correct:
            self._repository.fetch_task()
        else:
            self._repository.update_solution()
