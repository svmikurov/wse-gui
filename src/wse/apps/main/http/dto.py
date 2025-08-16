"""Defines Main app DAT."""

from datetime import datetime

from pydantic import BaseModel


class AssignedExercisesDTO(BaseModel):
    """Assigned exercises DTO."""

    assignation_id: str
    mentorship_id: str
    mentor_username: str
    exercise_id: str
    exercise_name: str
    count: int | None
    award: int | None
    is_active: bool | None
    is_daily: bool | None
    expiration: datetime | None
