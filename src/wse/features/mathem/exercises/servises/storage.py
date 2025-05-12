"""Defines task conditions storage."""

import logging

from wse.features.mathem.interfaces.iexercise import (
    ISimpleMathAnswer,
    ISimpleMathTask,
)

logger = logging.getLogger(__name__)


class TaskStorage:
    """Task conditions storage."""

    _task: ISimpleMathTask

    def __init__(self) -> None:
        """Construct the storage."""

    def save_task(self, task: ISimpleMathTask) -> None:
        """Save the conditions of an exercise task to storage."""
        self._task = task

    def retrieve_task(self) -> ISimpleMathTask:
        """Retrieve the conditions of an exercise task from storage."""
        return self._task

    @property
    def answer(self) -> ISimpleMathAnswer | None:
        """Retrieve from storage the correct answer."""
        try:
            task = self.retrieve_task()
        except AttributeError:
            logger.exception('A non-existent task was requested.')
            return None
        else:
            return task.answer
