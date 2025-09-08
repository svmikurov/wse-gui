"""Task data source."""

import logging
import uuid
from typing import Literal

from typing_extensions import override

from wse.data.sources import BaseTaskObserver
from wse.data.sources.base.source import DataSourceGen
from wse.data.sources.task.protocol import TaskSourceProto
from wse.feature.shared.schemas.task import Result

logger = logging.getLogger(__name__)

_NotifyType = Literal[
    'task_updated',
    'answer_correct',
    'answer_incorrect',
]


class TaskSource(
    DataSourceGen[BaseTaskObserver, _NotifyType],
    TaskSourceProto,
):
    """Task data."""

    def __init__(self) -> None:
        """Construct the task source."""
        super().__init__()
        self._uid: uuid.UUID | None = None
        self._question: str | None = None
        self._correct_answer: str | None = None
        self._is_correct: bool | None = None

    @override
    def set_task(self, uid: uuid.UUID, question: str) -> None:
        """Set task data."""
        self._uid = uid
        self._question = question
        self.notify('task_updated', uid=self._uid, question=self._question)
        logger.debug(f'Task updated, {question = }')

    @override
    def set_result(self, result: Result) -> None:
        """Set task result."""
        self._is_correct = result.is_correct
        self._correct_answer = result.correct_answer

        if self._is_correct:
            self._reset_task()
            self.notify('task_updated', uid=self._uid, question=self._question)
            self.notify('answer_correct')
        else:
            if self.correct_expression:
                self.notify('answer_incorrect', value=self.correct_expression)
            self._reset_task()

    @property
    @override
    def uid(self) -> uuid.UUID | None:
        """Get task identifier (read-only)."""
        return self._uid

    @property
    @override
    def correct_expression(self) -> str | None:
        """Get correct task expression."""
        if self._question and self._correct_answer:
            return f'{self._question} = {self._correct_answer}'
        return None

    def _reset_task(self) -> None:
        """Update task data."""
        self._uid = None
        self._question = None
        self._correct_answer = None
        self._is_correct = None
