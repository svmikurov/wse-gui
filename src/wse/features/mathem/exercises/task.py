"""Defines task conditions."""

from dataclasses import dataclass
from typing import Callable

from wse.interface.iexercise import ITask, ITaskStorage


class UserAnswer:
    """The user text answer."""

    def __init__(self, text: str) -> None:
        """Construct the answer."""
        self._text = text

    @property
    def text(self) -> str:
        """Return a string representation of the answer."""
        return self._text


# NOTE: Currently unused, but kept for potential future needs.
#       Possible use cases:
#       - Integration with advanced math operations
@dataclass
class TaskManager:
    """Manages task lifecycle and storage operations."""

    storage: ITaskStorage
    exercise_factory: Callable  # Task creation strategy

    def create_new_task(self) -> ITask:
        """Generate and store new task."""
        task = self.exercise_factory()
        self.storage.save_task(task)
        return task

    def get_current_task(self) -> ITask:
        """Retrieve current or generate new task."""
        if task := self.storage.retrieve_task():
            return task
        return self.create_new_task()
