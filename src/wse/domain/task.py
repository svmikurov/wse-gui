"""Task Use Cases."""

from injector import inject
from typing_extensions import override
from wse_exercises.core import MathEnum

from ..data.repositories.abc import CalculationTaskRepoABC
from ..data.repositories.calculation_exercises import CalculationExerciseRepo
from ..data.sources.task import (
    TaskObserverABC,
)
from .abc import (
    CheckCalculationAnswerUseCaseABC,
    GetCalculationQuestionUseCaseABC,
)


class SetCalculationExerciseUseCase:
    """Use Case for set current Calculation exercise."""

    @inject
    def __init__(self, repository: CalculationExerciseRepo) -> None:
        """Construct the case."""
        self._repository = repository

    def set_default(self, exercise: MathEnum) -> None:
        """Set Calculation exercise as default."""
        self._repository.set_default(exercise)


class CalculationObserverRegistryUseCase:
    """Use Case for subscribing to calculation task events."""

    @inject
    def __init__(self, repository: CalculationTaskRepoABC) -> None:
        """Construct the case."""
        self._repository = repository

    def register_observer(self, observer: TaskObserverABC) -> None:
        """Register an observer to receive calculation task updates."""
        self._repository.add_observer(observer)


class UpdateQuestionUseCase(
    GetCalculationQuestionUseCaseABC,
):
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


class CheckCalculationUseCase(
    CheckCalculationAnswerUseCaseABC,
):
    """Check calculation exercise user task answer Use Case."""

    @override
    def check(self, answer: str) -> None:
        """Check user answer."""
        self._repository.fetch_result(answer)
