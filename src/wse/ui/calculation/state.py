"""Calculation exercise ModelView."""

import uuid
from dataclasses import dataclass

import toga
from injector import inject
from typing_extensions import Literal, override

from wse.apps.nav_id import NavID
from wse.core.interfaces import Navigable
from wse.data.sources import BaseTaskObserver, TaskSource
from wse.domain import (
    CheckCalculationUseCaseProto,
    GetQuestionUseCaseProto,
)
from wse.feature.base.mixins import AddObserverGen

from .abc import BaseCalculationModelView

_NotifyType = Literal[
    'question_updated',
    'answer_updated',
    'answer_incorrect',
    'state_reset',
]


@inject
@dataclass
class CalculationModelView(
    AddObserverGen[_NotifyType],
    BaseCalculationModelView,
    BaseTaskObserver,
):
    """Calculation exercise ModelView."""

    _question_case: GetQuestionUseCaseProto
    _result_case: CheckCalculationUseCaseProto
    _navigator: Navigable
    _task_data: TaskSource

    def __post_init__(self) -> None:
        """Construct the view state."""
        self._task_uid: uuid.UUID | None = None
        self._question: str | None = None
        self._user_answer: str | None = None
        self._task_data.add_listener(self)

    # API

    @override
    def start_task(self) -> None:
        """Start new task."""
        self._reset_state()
        self._question_case.fetch()

    @override
    def update_answer(self, value: str) -> None:
        """Update user answer."""
        self._user_answer = value
        self._notify('answer_updated', value=value)

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
    def updated_task(self, _: toga.Button) -> None:
        """Get next task."""
        self.start_task()

    # Task Source observe

    @override
    def task_updated(self, uid: uuid.UUID, question: str) -> None:
        """Update question."""
        self._task_uid = uid
        self._question = question
        self._notify('question_updated', value=question)

    @override
    def answer_incorrect(self, value: str) -> None:
        """Handle the incorrect answer event."""
        self._notify('answer_incorrect', value=value)

    @override
    def answer_correct(self) -> None:
        """Handle the correct answer event."""
        self._reset_state()
        self.start_task()

    # Utility methods

    def _reset_state(self) -> None:
        """Reset UI state."""
        self._task_uid = None
        self._question = None
        self._user_answer = None
        self._notify('state_reset')
