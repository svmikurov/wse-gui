"""Abstract base class for exercise model."""

from abc import ABC, abstractmethod

from typing_extensions import override

from .protocol import ExerciseModelProto, ExerciseT_contra


class BaseExerciseModel(
    ABC,
    ExerciseModelProto[ExerciseT_contra],
):
    """Abstract base class for exercise page model."""

    @abstractmethod
    @override
    def set_exercise(self, exercise: ExerciseT_contra) -> None:
        """Set the exercise with and it conditions."""

    @abstractmethod
    @override
    def update_task(self) -> None:
        """Start or update task."""

    @abstractmethod
    @override
    def set_answer(self, value: str) -> None:
        """Set the entered user answer."""

    @abstractmethod
    @override
    def check_answer(self) -> None:
        """Check the user's submitted answer."""
