"""Protocol for exercises API."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from wse.core.api import ExerciseApiProto

from .schema import Assigned, ExerciseMeta

if TYPE_CHECKING:
    from . import ExerciseInfo


class AssignationsApiProto(Protocol):
    """Protocol for assigned exercises API interface."""

    def request_all_exercises(self) -> list[ExerciseInfo] | None:
        """Request all assigned by mentors exercises."""

    def request_selected(self, assignation_id: str) -> ExerciseMeta | None:
        """Request selected exercise."""


class AssignedApiProto(
    ExerciseApiProto[Assigned],
    Protocol,
):
    """Protocol for assigned exercise API client interface."""
