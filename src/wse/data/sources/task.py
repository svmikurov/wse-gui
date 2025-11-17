"""Task data source."""

from abc import ABC, abstractmethod
from dataclasses import replace
from typing import Literal, Union

from wse.api.schemas.task import Question, Result
from wse.data.entities.task import Task
from wse.data.sources.base.source import SourceGen

_NotifyType = Literal[
    'question_updated',
    'result_updated',
    'solution_updated',
]

TaskObserverT = Union[
    'ResultObserverABC',
    'TaskObserverABC',
]


class ResultObserverABC(ABC):
    """ABC for task source 'result update' event observer."""

    @abstractmethod
    def result_updated(self, is_correct: bool) -> None:
        """Handle the 'result updated' task source event."""


class TaskObserverABC(
    ResultObserverABC,
    ABC,
):
    """ABC for task source observer."""

    @abstractmethod
    def question_updated(self, question: str) -> None:
        """Handle the 'question updated' task source event."""

    @abstractmethod
    def solution_updated(self, solution: str) -> None:
        """Handle the 'solution updated' task source event."""


class TaskSource(
    SourceGen[
        TaskObserverT,
        _NotifyType,
    ],
):
    """Task data."""

    def __init__(self) -> None:
        """Construct the task source."""
        super().__init__()
        self._task: Task | None = None

    def update_task(self, data: Question) -> None:
        """Set task data."""
        self._task = Task(**data.to_dict())
        self.notify('question_updated', question=self._task.question)

    def update_result(self, result: Result) -> None:
        """Set task result."""
        if self._task is None:
            raise AttributeError('The task was not set')

        self._task = replace(self._task, **result.to_dict())
        self.notify('result_updated', is_correct=self._task.is_correct)

    def update_solution(self) -> None:
        """Set task solution."""
        if self._task is None:
            raise AttributeError('The task was not set')

        self._task = replace(self._task, solution=self.solution)
        self.notify('solution_updated', solution=self.solution)

    @property
    def uid(self) -> str | None:
        """Get task identifier (read-only)."""
        return self._task.uid if self._task is not None else None

    @property
    def solution(self) -> str:
        """Get correct task expression."""
        if not self._task or not self._task.correct_answer:
            raise AttributeError(f'Get solution error, task={self._task}')

        return f'{self._task.question} = {self._task.correct_answer}'

    def _reset_task(self) -> None:
        """Update task data."""
        self._task = None
