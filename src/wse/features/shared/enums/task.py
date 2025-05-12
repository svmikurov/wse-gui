"""Defines possible states of exercise."""

from wse.core.base import BaseEnum


class TaskState(BaseEnum):
    """Represents possible states of exercise."""

    QUESTION = 'Question generated'
    FAILED = 'Verification failed'
    NO_TASK = 'No active task'
    ANSWER_CHECKING = 'Answer checking'
