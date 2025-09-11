"""Abstract base class for assigned exercises API."""

from abc import ABC, abstractmethod

from wse.feature.shared.schemas.exercise import ExerciseInfo, ExerciseMeta


class AssignationsApiABC(ABC):
    """Abstract base class for assigned exercises API."""

    @abstractmethod
    def request_all_exercises(self) -> list[ExerciseInfo] | None:
        """Request all assigned by mentors exercises."""

    @abstractmethod
    def request_selected(self, assignation_id: str) -> ExerciseMeta | None:
        """Request selected exercise."""
