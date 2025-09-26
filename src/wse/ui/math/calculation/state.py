"""Calculation exercise UI state."""

from dataclasses import dataclass

from injector import inject

from wse.core.interfaces import Navigable
from wse.domain.abc.calculation import (
    CheckCalculationAnswerUseCaseABC,
    GetCalculationQuestionUseCaseABC,
    GetCalculationSolutionUseCaseABC,
)
from wse.domain.math_task import CalculationObserverRegistryUseCase

from ...base.navigate.mixin import NavigateStateMixin
from ...base.task.state import TaskState, TaskViewModelMixin
from .abc import CalculationViewModelABC


@dataclass(frozen=True)
class CalculationUIState(TaskState):
    """Calculation exercise UI state data."""


@inject
@dataclass
class CalculationViewModel(
    NavigateStateMixin,
    TaskViewModelMixin,
    CalculationViewModelABC,
):
    """Calculation exercise ViewModel."""

    _navigator: Navigable

    _question_case: GetCalculationQuestionUseCaseABC
    _result_case: CheckCalculationAnswerUseCaseABC
    _solution_case: GetCalculationSolutionUseCaseABC

    _source_observer_case: CalculationObserverRegistryUseCase

    def __post_init__(self) -> None:
        """Construct the view state."""
        self._data = CalculationUIState()
        self._source_observer_case.register_observer(self)

    # On screen close event

    def on_close(self) -> None:
        """Call methods before close the screen."""
        self._source_observer_case.remove_observer(self)
