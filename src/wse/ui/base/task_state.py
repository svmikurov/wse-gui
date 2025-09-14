"""Base UI state for task."""

from typing import Callable, Literal

import toga

from wse.core.interfaces import Navigable
from wse.domain.abc import CheckAnswerUseCaseABC, GetQuestionUseCaseABC
from wse.feature.base.mixins import AddObserverGenT
from wse.ui.base.task import TaskViewModelObserverABC

_StateNotifyT = Literal[
    'question_updated',
    'answer_updated',
    'answer_incorrect',
    'solution_updated',
]


class TaskViewModelMixin(
    AddObserverGenT[TaskViewModelObserverABC, _StateNotifyT],
):
    """Mixin providing Task feature for ViewModel."""

    _navigator: Navigable

    _question_case: GetQuestionUseCaseABC
    _result_case: CheckAnswerUseCaseABC

    _notify: Callable[..., None]
    _update_data: Callable[..., None]
    _reset_data: Callable[..., None]

    # Feature API

    def start_task(self) -> None:
        """Start new task."""
        self._reset_data()
        self._question_case.update()

    def update_answer(self, value: str) -> None:
        """Update user answer."""
        self._update_data(answer=value)
        self._notify('answer_updated', answer=value)

    # Callback methods

    # TODO: Fix type ignore
    def submit_answer(self, _: toga.Button) -> None:
        """Submit user answer."""
        if self._data.answer:  # type: ignore[attr-defined]
            self._result_case.check(self._data.answer)  # type: ignore[attr-defined]

    def update_task(self, _: toga.Button) -> None:
        """Get next task."""
        self.start_task()

    # Task source observe

    def question_updated(self, question: str) -> None:
        """Handle the 'task updated' source event."""
        self._reset_data()
        self._update_data(question=question)
        self._notify('question_updated', question=question)

    def result_updated(self, is_correct: bool) -> None:
        """Handle the correct answer event."""
        if not is_correct:
            self._notify('answer_incorrect')

    def solution_updated(self, solution: str) -> None:
        """Handle the 'solution updated' the source event."""
        self._update_data(solution=solution)
        self._notify('solution_updated', solution=solution)
