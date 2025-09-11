"""Task Use Cases."""

from injector import inject
from typing_extensions import override
from wse_exercises.core import MathEnum

from ..data.repositories.calculation_exercise import CalculationExerciseRepo
from ..data.repositories.calculation_task import CalculationTaskRepo
from ..data.repositories.protocol import CalculationRepoProto
from ..data.sources.task import (
    ResultObserverABC,
    TaskObserverABC,
)
from .abc import CheckCalculationUseCaseABC, GetQuestionUseCaseABC


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
    def __init__(self, repository: CalculationTaskRepo) -> None:
        """Construct the case."""
        self._repository = repository

    def register_observer(self, observer: TaskObserverABC) -> None:
        """Register an observer to receive calculation task updates."""
        self._repository.add_observer(observer)


class UpdateQuestionUseCase(
    GetQuestionUseCaseABC,
):
    """Fetch calculation exercise task question Use Case."""

    @inject
    def __init__(
        self,
        repository: CalculationRepoProto,
    ) -> None:
        """Construct the case."""
        super().__init__(repository)

    @override
    def update(self) -> None:
        """Get task question."""
        self._repository.fetch_task()


class CheckCalculationUseCase(
    CheckCalculationUseCaseABC,
):
    """Check calculation exercise user task answer Use Case."""

    @override
    def check(self, answer: str) -> None:
        """Check user answer."""
        self._repository.fetch_result(answer)


class CalculationLogicUseCase(ResultObserverABC):
    """Calculation exercise logic."""

    @inject
    def __init__(
        self,
        repository: CalculationTaskRepo,
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
