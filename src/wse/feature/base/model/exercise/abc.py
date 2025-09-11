"""Abstract base class for exercise model."""

from abc import ABC, abstractmethod
from typing import Generic

from .protocol import ExerciseT_contra


class ExerciseModelABC(
    ABC,
    Generic[ExerciseT_contra],
):
    """Abstract base class for exercise page model."""

    @abstractmethod
    def set_exercise(self, exercise: ExerciseT_contra) -> None:
        """Set the exercise with and it conditions."""

    @abstractmethod
    def update_task(self) -> None:
        """Start or update task."""

    @abstractmethod
    def set_answer(self, value: str) -> None:
        """Set the entered user answer."""

    @abstractmethod
    def check_answer(self) -> None:
        """Check the user's submitted answer."""
