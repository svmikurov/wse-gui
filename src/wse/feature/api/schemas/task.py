"""Service entities."""

import uuid

from ..schemas.base import BaseSchema


class Question(BaseSchema):
    """Question schema."""

    uid: uuid.UUID
    question: str

    class Config:
        """Model configuration."""

        extra = 'forbid'


class Answer(BaseSchema):
    """User answer schema."""

    uid: uuid.UUID
    answer: str

    class Config:
        """Model configuration."""

        extra = 'forbid'


class Result(BaseSchema):
    """Answer check result."""

    is_correct: bool
    correct_answer: str | None = None
    user_answer: str | None = None

    class Config:
        """Model configuration."""

        extra = 'forbid'
