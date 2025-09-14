"""Calculation exercise ViewModel."""

from dataclasses import dataclass, replace
from typing import TypedDict

from injector import inject
from typing_extensions import Unpack

from wse.core.interfaces import Navigable
from wse.domain.abc import (
    CheckCalculationAnswerUseCaseABC,
    GetCalculationQuestionUseCaseABC,
)
from wse.domain.task import CalculationObserverRegistryUseCase
from wse.domain.task_logic import CalculationLogicUseCase
from wse.ui.base.task_state import TaskViewModelMixin

from ...base.mixin import NavigateMixin
from .abc import CalculationViewModelABC


class _DataFieldType(TypedDict, total=False):
    """Field types for Calculation UI state data."""

    question: str
    answer: str
    solution: str
    balance: str


@dataclass(frozen=True)
class _CalculationUIState:
    """Calculation UI state data."""

    question: str | None = None
    answer: str | None = None
    solution: str | None = None
    balance: str | None = None


@inject
@dataclass
class CalculationViewModel(
    NavigateMixin,
    TaskViewModelMixin,
    CalculationViewModelABC,
):
    """Calculation exercise ViewModel."""

    _navigator: Navigable

    _question_case: GetCalculationQuestionUseCaseABC
    _result_case: CheckCalculationAnswerUseCaseABC
    _logic_case: CalculationLogicUseCase

    _source_observer_case: CalculationObserverRegistryUseCase

    def __post_init__(self) -> None:
        """Construct the view state."""
        self._create_data()
        self._source_observer_case.register_observer(self)

    def _create_data(self) -> None:
        """Create UI state data."""
        self._data = _CalculationUIState()

    def _update_data(self, **data: Unpack[_DataFieldType]) -> None:
        """Update UI state data."""
        self._data = replace(self._data, **data)

    def _reset_data(self) -> None:
        """Reset UI state data."""
        self._create_data()
        self._notify('state_reset')
