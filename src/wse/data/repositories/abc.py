"""Abstract base class for repository."""

from abc import ABC, abstractmethod

from wse.data.sources.task import TaskObserverT


class TaskRepoABC(ABC):
    """ABC for task repository."""

    @abstractmethod
    def fetch_task(self) -> None:
        """Fetch task question."""

    @abstractmethod
    def fetch_result(self, answer: str) -> None:
        """Fetch user answer check result."""

    # TODO: Move to mixin
    @abstractmethod
    def add_observer(self, listener: TaskObserverT) -> None:
        """Subscribe listener to repository notifications."""

    @abstractmethod
    def remove_observer(self, listener: TaskObserverT) -> None:
        """Remove listener from repository notifications."""

    @abstractmethod
    def update_solution(self) -> None:
        """Set current solution."""


class CalculationTaskRepoABC(TaskRepoABC, ABC):
    """ABC for Calculation exercise repository."""


class AssignedTaskRepoABC(TaskRepoABC, ABC):
    """ABC for Assigned exercise repository."""
