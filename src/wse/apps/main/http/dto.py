"""Defines Main app DAT."""

from datetime import datetime

from pydantic import BaseModel


class AssignedExercisesDTO(BaseModel):
    """Assigned exercises DTO."""

    mentorship_id: int
    exercise_id: int
    exercise_name: str
    count: int | None
    award: int | None
    is_active: bool | None
    is_daily: bool | None
    expiration: datetime | None
