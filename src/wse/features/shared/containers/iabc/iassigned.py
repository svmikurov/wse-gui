"""Defines protocol and ABC for the container of Assigned exercises."""

from abc import ABC, abstractmethod
from typing import Protocol

from typing_extensions import override

from wse.apps.main.http.dto import AssignedExercisesDTO
from wse.features.interfaces.icontent import IGetContent
from wse.features.interfaces.iobserver import ISubject


class IAssignedContainer(
    ISubject,
    IGetContent,
    Protocol,
):
    """Protocol for the container interface of Assigned exercises."""

    def add_exercise(self, exercise: AssignedExercisesDTO) -> None:
        """Add exercise to display.

        Groups the exercise by mentor.

        :param AssignedExercisesDTO exercise: Assigned exercise
        """

    def update_exercises(self, exercises: list[AssignedExercisesDTO]) -> None:
        """Update exercises.

        :param list[AssignedExercisesDTO] exercises: Exercises to update
        """

    def remove_exercises(self) -> None:
        """Remove all exercises."""


class AssignedContainerABC(IAssignedContainer, ABC):
    """Abstract base class for the container of Assigned exercises."""

    @abstractmethod
    @override
    def add_exercise(self, exercise: AssignedExercisesDTO) -> None:
        """Add exercise to choice."""

    @abstractmethod
    @override
    def update_exercises(self, exercises: list[AssignedExercisesDTO]) -> None:
        """Update exercises."""

    @abstractmethod
    @override
    def remove_exercises(self) -> None:
        """Remove all exercises."""
