"""Defines ABC for the container of Assigned exercises."""

from abc import ABC, abstractmethod

from wse.data.schemas.exercise import ExerciseInfo
from wse.ui.base.content.abc import GetContentABC


class AssignationsContainerABC(
    GetContentABC,
    ABC,
):
    """Abstract base class for the container of Assigned exercises."""

    @abstractmethod
    def add_exercise(self, exercise: ExerciseInfo) -> None:
        """Add exercise to choice."""

    @abstractmethod
    def update_exercises(self, exercises: list[ExerciseInfo]) -> None:
        """Update exercises."""

    @abstractmethod
    def remove_exercises(self) -> None:
        """Remove all exercises."""

    @abstractmethod
    def add_observer(self, observer: object) -> None:
        """Add an observer to receive task updates."""

    @abstractmethod
    def remove_observer(self, observer: object) -> None:
        """Remove observer from subject observers."""
