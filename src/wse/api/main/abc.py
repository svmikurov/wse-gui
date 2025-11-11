"""Abstract base class for assigned exercises API."""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from wse.feature.services import Answer

from .. import responses
from ..schemas import exercise

ExerciseT_contra = TypeVar(
    'ExerciseT_contra',
    contravariant=True,
    bound=exercise.ExerciseMeta,
)


class ExerciseApiABC(ABC, Generic[ExerciseT_contra]):
    """Protocol for exercise API client interface."""

    @abstractmethod
    def request_task(
        self,
        exercise: ExerciseT_contra,
    ) -> responses.QuestionResponse | None:
        """Request a task from the server."""

    @abstractmethod
    def check_answer(
        self,
        answer: Answer,
        exercise: ExerciseT_contra,
    ) -> responses.ResultResponse | None:
        """Check on the server the user's entered answer."""


class AssignationsApiABC(ABC):
    """Abstract base class for assigned exercises API."""

    @abstractmethod
    def request_all_exercises(
        self,
    ) -> list[exercise.ExerciseInfo] | None:
        """Request all assigned by mentors exercises."""

    @abstractmethod
    def request_selected(
        self,
        assignation_id: str,
    ) -> exercise.Assigned | None:
        """Request selected exercise."""


class AssignedApiABC(
    ExerciseApiABC[exercise.Assigned],
    ABC,
):
    """ABC for Assigned exercise api client with text task."""
