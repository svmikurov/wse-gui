"""Protocol for exercises API."""

from __future__ import annotations

from typing import Protocol

from wse.core.api.protocol import ExerciseApiProto
from wse.feature.api.schemas.exercise import (
    Assigned,
    ExerciseInfo,
    ExerciseMeta,
)


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
