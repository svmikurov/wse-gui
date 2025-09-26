"""Defines protocol for API client interface."""

from typing import Protocol, TypeVar

from wse.feature.api.schemas.exercise import ExerciseMeta
from wse.feature.services import Answer

from .response import QuestionResponse, ResultResponse

ExerciseT_contra = TypeVar(
    'ExerciseT_contra',
    contravariant=True,
    bound=ExerciseMeta,
)


class AuthAPIjwtProto(Protocol):
    """Protocol for authentication API interface."""

    def obtain_tokens(self, username: str, password: str) -> dict[str, str]:
        """Obtain 'refresh' and 'access' tokens."""

    def check_access_token(self, access_token: str) -> bool:
        """Check the access token."""

    def refresh_access_token(self, refresh_token: str) -> str:
        """Refresh the 'access' token."""


class ExerciseApiProto(Protocol[ExerciseT_contra]):
    """Protocol for exercise API client interface."""

    def request_task(
        self,
        exercise: ExerciseT_contra,
    ) -> QuestionResponse | None:
        """Request a task from the server."""

    def check_answer(
        self,
        answer: Answer,
        exercise: ExerciseT_contra,
    ) -> ResultResponse | None:
        """Check on the server the user's entered answer."""
