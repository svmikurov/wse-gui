"""Defines task conditions storage."""

import logging

from wse.interface.iexercise import IAnswer, IExercise

logger = logging.getLogger(__name__)


class TaskStorage:
    """Task conditions storage."""

    def __init__(self) -> None:
        """Construct the storage."""
        self._task = None

    def save_task(self, task: IExercise) -> None:
        """Save the conditions of an exercise task to storage."""
        self._task = task

    def retrieve_task(self) -> IExercise:
        """Retrieve the conditions of an exercise task from storage."""
        return self._task

    @property
    def answer(self) -> IAnswer:
        """Retrieve from storage the correct answer."""
        return self.retrieve_task().answer
