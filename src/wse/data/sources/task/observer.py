"""Abstract base class for task observer."""

import uuid
from abc import ABC, abstractmethod
from typing import Protocol


class TaskObserverProto(Protocol):
    """Task observer."""

    def task_updated(self, uid: uuid.UUID, question: str) -> None:
        """Handle the task updated event."""

    def answer_incorrect(self, value: str) -> None:
        """Handle the incorrect answer event."""

    def answer_correct(self) -> None:
        """Handle the correct answer event."""


class BaseTaskObserver(ABC):
    """Task observer."""

    @abstractmethod
    def task_updated(self, uid: uuid.UUID, question: str) -> None:
        """Handle the task updated event."""

    @abstractmethod
    def answer_incorrect(self, value: str) -> None:
        """Handle the incorrect answer event."""

    @abstractmethod
    def answer_correct(self) -> None:
        """Handle the correct answer event."""
