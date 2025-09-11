"""Calculation exercise ViewModel."""

from dataclasses import dataclass, replace
from typing import TypedDict

import toga
from injector import inject
from typing_extensions import Literal, Unpack, override

from wse.apps.nav_id import NavID
from wse.core.interfaces import Navigable
from wse.data.sources.task import TaskObserverABC
from wse.domain.protocol import (
    CheckCalculationUseCaseProto,
    UpdateQuestionUseCaseProto,
)
from wse.domain.task import (
    CalculationLogicUseCase,
    CalculationObserverRegistryUseCase,
)
from wse.feature.base.mixins import AddObserverGen

from .abc import CalculationViewModelABC

_NotifyType = Literal[
    'question_updated',
    'answer_updated',
    'answer_incorrect',
    'solution_updated',
    'state_reset',
]


class DataFieldType(TypedDict, total=False):
    """Field types for Calculation UI state data."""

    question: str
    answer: str
    solution: str


@dataclass(frozen=True)
class CalculationUIState:
    """Calculation UI state data.

    The UI state data is immutable.
    """

    question: str | None = None
    answer: str | None = None
    solution: str | None = None


@inject
@dataclass
class CalculationViewModel(
    AddObserverGen[_NotifyType],
    CalculationViewModelABC,
    TaskObserverABC,
):
    """Calculation exercise ViewModel."""

    _navigator: Navigable

    _question_case: UpdateQuestionUseCaseProto
    _result_case: CheckCalculationUseCaseProto
    _source_observer_case: CalculationObserverRegistryUseCase
    _logic_case: CalculationLogicUseCase

    def __post_init__(self) -> None:
        """Construct the view state."""
        self._data = CalculationUIState()
        self._source_observer_case.register_observer(self)

    @override
    def start_task(self) -> None:
        """Start new task."""
        self._reset_data()
        self._question_case.update()

    @override
    def update_answer(self, answer: str) -> None:
        """Update user answer."""
        self._update_data(answer=answer)
        self._notify('answer_updated', answer=answer)

    @override
    def navigate(self, nav_id: NavID) -> None:
        """Handle the navigate event, callback."""
        self._navigator.navigate(nav_id=nav_id)

    # Callback methods

    @override
    def submit_answer(self, _: toga.Button) -> None:
        """Submit user answer."""
        if self._data.answer:
            self._result_case.check(self._data.answer)

    @override
    def update_task(self, _: toga.Button) -> None:
        """Get next task."""
        self.start_task()

    # Task source observe

    @override
    def question_updated(self, question: str) -> None:
        """Handle the 'task updated' source event."""
        self._reset_data()
        self._update_data(question=question)
        self._notify('question_updated', question=question)

    @override
    def result_updated(self, is_correct: bool) -> None:
        """Handle the correct answer event."""
        if not is_correct:
            self._notify('answer_incorrect')

    @override
    def solution_updated(self, solution: str) -> None:
        """Handle the 'solution updated' the source event."""
        self._update_data(solution=solution)
        self._notify('solution_updated', solution=solution)

    # Utility methods

    def _reset_data(self) -> None:
        """Reset Calculation exercise UI state data."""
        self._data = CalculationUIState()
        self._notify('state_reset')

    def _update_data(self, **new_data: Unpack[DataFieldType]) -> None:
        """Update Calculation exercise UI state data."""
        self._data = replace(self._data, **new_data)
