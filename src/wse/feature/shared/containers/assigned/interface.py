"""Defines protocol and ABC for the container of Assigned exercises."""

from typing import Protocol

from wse.feature.interfaces.icontent import GetContentProto
from wse.feature.interfaces.iobserver import Observable
from wse.feature.shared.schemas.exercise import ExerciseInfo


class AssignationsContainerProto(
    Observable,
    GetContentProto,
    Protocol,
):
    """Protocol for the container interface of Assigned exercises."""

    def add_exercise(self, exercise: ExerciseInfo) -> None:
        """Add exercise to display.

        Groups the exercise by mentor.

        :param ExerciseInfo exercise: Assigned exercise
        """

    def update_exercises(self, exercises: list[ExerciseInfo]) -> None:
        """Update exercises.

        :param list[ExerciseInfo] exercises: Exercises to update
        """

    def remove_exercises(self) -> None:
        """Remove all exercises."""
