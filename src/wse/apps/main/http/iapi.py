"""Defines protocols and ABC for exercises API."""

from abc import abstractmethod
from typing import Protocol

from typing_extensions import override

from .dto import AssignedExerciseDTO


class IAssignedExercisesApi(Protocol):
    """Protocol for assigned exercises API interface."""

    def request_all_exercises(self) -> list[AssignedExerciseDTO]:
        """Request all assigned by mentors exercises."""


class AssignedExercisesABC(IAssignedExercisesApi):
    """Abstract base class for assigned exercises API."""

    @abstractmethod
    @override
    def request_all_exercises(self) -> list[AssignedExerciseDTO]:
        """Request all assigned by mentors exercises."""
