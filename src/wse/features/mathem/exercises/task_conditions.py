"""Defines task conditions."""

from wse.interface.iexercise import ITask, ITaskConditions


class TaskConditions(ITaskConditions):
    """Exercise task conditions."""

    def __init__(self) -> None:
        """Construct the task conditions."""
        self._task = None

    @property
    def task(self) -> ITask:
        """Exercise task."""
        return self._task

    @task.setter
    def task(self, value: ITask) -> None:
        self._task = value

    def __str__(self) -> str:
        """Return the string representation."""
        return str(self._task)
