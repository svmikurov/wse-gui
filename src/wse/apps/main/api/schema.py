"""Defines Main app DAT."""

from datetime import datetime

from wse.feature.base import BaseSchema


class ExerciseMeta(BaseSchema):
    """Exercise meta data."""

    class Config:
        """Model configuration."""

        extra = 'forbid'

    question_url_path: str
    check_url_path: str
    task_io: str


class Assigned(ExerciseMeta):
    """Assigned exercise meta data."""

    assignation_id: str


class ExerciseInfo(BaseSchema):
    """Assigned exercise information."""

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
