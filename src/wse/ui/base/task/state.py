"""Base UI state for task."""

from dataclasses import dataclass, replace
from typing import Literal, TypedDict

import toga
from typing_extensions import Unpack

from wse.core.interfaces import Navigable
from wse.data.sources.task import TaskObserverABC
from wse.feature.observer.mixins import SubjectGen

from ....domain.abc.task import (
    CheckAnswerUseCaseABC,
    GetQuestionUseCaseABC,
    GetSolutionUseCaseABC,
)
from .abc import TaskViewModelFeatureABC, TaskViewModelObserverABC

TaskNotifyT = Literal[
    'question_updated',
    'answer_updated',
    'answer_incorrect',
    'solution_updated',
    'task_reset',
]


class _DataFieldType(TypedDict, total=False):
    """Field types for Assigned exercise UI state data."""

    question: str | None
    answer: str | None
    solution: str | None


@dataclass(frozen=True)
class TaskState:
    """Exercise task UI state data."""

    question: str | None = None
    answer: str | None = None
    solution: str | None = None


class TaskViewModelMixin(
    SubjectGen[TaskViewModelObserverABC, TaskNotifyT],
    TaskViewModelFeatureABC,
    TaskObserverABC,
):
    """Mixin providing Task feature for ViewModel."""

    _navigator: Navigable

    _question_case: GetQuestionUseCaseABC
    _result_case: CheckAnswerUseCaseABC
    _solution_case: GetSolutionUseCaseABC

    _data: TaskState

    # Feature API

    def start_task(self) -> None:
        """Start new task."""
        self._reset_task_data()
        self._question_case.update()

    def update_answer(self, value: str) -> None:
        """Update user answer."""
        self._update_data(answer=value)
        self.notify('answer_updated', answer=value)

    # Button callback methods

    def submit_answer(self, _: toga.Button) -> None:
        """Submit user answer."""
        if self._data.answer:
            self._result_case.check(self._data.answer)

    def update_task(self, _: toga.Button) -> None:
        """Get next task."""
        self.start_task()

    # Task Data source observe

    def question_updated(self, question: str) -> None:
        """Handle the 'task updated' source event."""
        self._reset_task_data()
        self._update_data(question=question)
        self.notify('question_updated', question=question)

    def solution_updated(self, solution: str) -> None:
        """Handle the 'solution updated' the source event."""
        self._update_data(solution=solution)
        self.notify('solution_updated', solution=solution)

    def result_updated(self, is_correct: bool) -> None:
        """Handle the answer check result."""
        if is_correct:
            self.start_task()
        else:
            self.notify('answer_incorrect')
            self._solution_case.update_solution()

    # UI State data management

    def _update_data(self, **data: Unpack[_DataFieldType]) -> None:
        """Update UI state data."""
        self._data = replace(self._data, **data)

    def _reset_task_data(self) -> None:
        """Reset UI state data."""
        self._update_data(question=None, answer=None, solution=None)
        self.notify('task_reset')
