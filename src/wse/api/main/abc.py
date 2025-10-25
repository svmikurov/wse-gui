"""Abstract base class for assigned exercises API."""

from abc import ABC, abstractmethod

from wse.api.schemas.exercise import Assigned, ExerciseInfo
from wse.core.api.base import ExerciseApi


class AssignationsApiABC(ABC):
    """Abstract base class for assigned exercises API."""

    @abstractmethod
    def request_all_exercises(self) -> list[ExerciseInfo] | None:
        """Request all assigned by mentors exercises."""

    @abstractmethod
    def request_selected(self, assignation_id: str) -> Assigned | None:
        """Request selected exercise."""


class AssignedApiClientABC(
    ExerciseApi[Assigned],
    ABC,
):
    """ABC for Assigned exercise api client with text task."""
