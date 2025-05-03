"""Defines task conditions storage."""

import logging

from wse.interface.iexercise import ITaskConditions

logger = logging.getLogger(__name__)


class TaskConditionsStorage:
    """Task conditions storage."""

    def __init__(self) -> None:
        """Construct the storage."""
        self._task_conditions = None

    def save_task_conditions(self, task_conditions: ITaskConditions) -> None:
        """Save the task conditions."""
        self._task_conditions = task_conditions
        logger.info(f'Saved task conditions: {task_conditions}')
