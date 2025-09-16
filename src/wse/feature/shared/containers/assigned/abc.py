"""Defines ABC for the container of Assigned exercises."""

from abc import ABC, abstractmethod

from wse.feature.base.abstract.mixins import GetContentABC
from wse.feature.interfaces.iobserver import ObserverProto
from wse.feature.shared.schemas.exercise import ExerciseInfo


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
    def add_observer(self, observer: ObserverProto) -> None:
        """Add an observer to receive task updates."""

    @abstractmethod
    def remove_observer(self, observer: ObserverProto) -> None:
        """Remove observer from subject observers."""
