"""Task business logic Use Cases."""

from dataclasses import dataclass

from injector import inject

from ..data.repositories.abc import TaskRepoABC
from ..data.repositories.assigned_task import AssignedTaskRepo
from ..data.repositories.calculation_task import CalculationTaskRepo
from ..data.sources.task import ResultObserverABC


@dataclass
class BaseTaskLogicUseCase(ResultObserverABC):
    """Base exercise task logic Use Case."""

    _repository: TaskRepoABC

    def __post_init__(self) -> None:
        """Construct the case."""
        self._repository.add_observer(self)

    def result_updated(self, is_correct: bool) -> None:
        """Handle the answer check result."""
        if is_correct:
            self._repository.fetch_task()
        else:
            self._repository.update_solution()


@inject
@dataclass
class CalculationLogicUseCase(BaseTaskLogicUseCase):
    """Calculation exercise logic Use Case."""

    _repository: CalculationTaskRepo


@inject
@dataclass
class AssignedLogicUseCase(BaseTaskLogicUseCase):
    """Assigned exercise logic Use Case."""

    _repository: AssignedTaskRepo
