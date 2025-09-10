"""Calculation exercise ViewModel."""

from dataclasses import dataclass

import toga
from injector import inject
from typing_extensions import Literal, override

from wse.apps.nav_id import NavID
from wse.core.interfaces import Navigable
from wse.data.sources.task import TaskSourceObserveABC
from wse.domain import (
    CheckCalculationUseCaseProto,
    UpdateQuestionUseCaseProto,
)
from wse.domain.task import (
    CalculationLogicUseCase,
    SubscribeExerciseSourceUseCase,
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


@inject
@dataclass
class CalculationViewModel(
    AddObserverGen[_NotifyType],
    CalculationViewModelABC,
    TaskSourceObserveABC,
):
    """Calculation exercise ViewModel."""

    _navigator: Navigable

    _question_case: UpdateQuestionUseCaseProto
    _result_case: CheckCalculationUseCaseProto
    _logic_case: CalculationLogicUseCase
    _source_proxy: SubscribeExerciseSourceUseCase

    def __post_init__(self) -> None:
        """Construct the view state."""
        self._source_proxy.subscribe(self)

        # Related data
        self._question: str | None = None
        self._user_answer: str | None = None
        self._solution: str | None = None

    # API

    @override
    def start_task(self) -> None:
        """Start new task."""
        self._reset_state()
        self._question_case.update()

    @override
    def update_answer(self, answer: str) -> None:
        """Update user answer."""
        self._user_answer = answer
        self._notify('answer_updated', answer=answer)

    @override
    def navigate(self, nav_id: NavID) -> None:
        """Handle the navigate event, callback."""
        self._navigator.navigate(nav_id=nav_id)

    # Callback methods

    @override
    def submit_answer(self, _: toga.Button) -> None:
        """Submit user answer."""
        if self._user_answer:
            self._result_case.check(self._user_answer)

    @override
    def update_task(self, _: toga.Button) -> None:
        """Get next task."""
        self.start_task()

    # Task Source observe

    @override
    def question_updated(self, question: str) -> None:
        """Handle the 'task updated' source event."""
        self._reset_state()
        self._question = question
        self._notify('question_updated', question=question)

    @override
    def result_updated(self, is_correct: bool) -> None:
        """Handle the correct answer event."""
        if not is_correct:
            self._notify('answer_incorrect')

    def solution_updated(self, solution: str) -> None:
        """Handle the 'solution updated' the source event."""
        self._solution = solution
        self._notify('solution_updated', solution=solution)

    # Utility methods

    def _reset_state(self) -> None:
        """Reset UI state."""
        self._question = None
        self._user_answer = None
        self._solution = None
        self._notify('state_reset')
