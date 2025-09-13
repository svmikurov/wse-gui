"""Assigned exercise UI state."""

from dataclasses import dataclass, replace
from typing import TypedDict

from injector import inject
from typing_extensions import Unpack

from wse.core.interfaces import Navigable
from wse.data.sources.assigned import AssignedSourceObserverABC
from wse.domain.abc import UserObserverRegistryUseCaseABC
from wse.domain.assigned import AssignedObserverRegistryUseCase
from wse.domain.task import CalculationLogicUseCase

from .abc import AssignedViewModelABC


class _DataFieldType(TypedDict, total=False):
    """Field types for Assigned exercise UI state data."""

    question: str
    answer: str
    solution: str
    balance: str


@dataclass(frozen=True)
class ExerciseUIState:
    """Assigned exercise UI state data.

    The UI state data is immutable.
    """

    question: str | None = None
    answer: str | None = None
    solution: str | None = None
    balance: str | None = None


@inject
@dataclass
class AssignedViewModel(
    AssignedSourceObserverABC,
    AssignedViewModelABC,
):
    """Assigned exercise ViewModel."""

    _navigator: Navigable

    # _question_case: UpdateQuestionUseCaseProto
    # _result_case: CheckCalculationUseCaseProto
    _logic_case: CalculationLogicUseCase

    _source_observer_case: AssignedObserverRegistryUseCase
    _user_observer_registry: UserObserverRegistryUseCaseABC

    def __post_init__(self) -> None:
        """Construct the state."""
        self._create_data()
        self._source_observer_case.register_observer(self)
        self._user_observer_registry.register_observer(self)

    # Utility methods

    def _create_data(self) -> None:
        """Create UI state data."""
        self._data = ExerciseUIState()

    def _update_data(self, **data: Unpack[_DataFieldType]) -> None:
        """Update UI state data."""
        replace(self._data, **data)
