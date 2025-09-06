"""Abstract base class for assigned exercises API."""

from abc import abstractmethod

from typing_extensions import override

from wse.feature.shared.schemas.exercise import ExerciseInfo, ExerciseMeta

from . import AssignationsApiProto


class BaseAssignationsApi(AssignationsApiProto):
    """Abstract base class for assigned exercises API."""

    @abstractmethod
    @override
    def request_all_exercises(self) -> list[ExerciseInfo] | None:
        """Request all assigned by mentors exercises."""

    @abstractmethod
    @override
    def request_selected(self, assignation_id: str) -> ExerciseMeta | None:
        """Request selected exercise."""
