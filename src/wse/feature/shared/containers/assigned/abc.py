"""Defines ABC for the container of Assigned exercises."""

from abc import ABC, abstractmethod

from typing_extensions import override

from wse.feature.shared.schemas.exercise import ExerciseInfo

from . import AssignationsContainerProto


class AssignationsContainerABC(AssignationsContainerProto, ABC):
    """Abstract base class for the container of Assigned exercises."""

    @abstractmethod
    @override
    def add_exercise(self, exercise: ExerciseInfo) -> None:
        """Add exercise to choice."""

    @abstractmethod
    @override
    def update_exercises(self, exercises: list[ExerciseInfo]) -> None:
        """Update exercises."""

    @abstractmethod
    @override
    def remove_exercises(self) -> None:
        """Remove all exercises."""
