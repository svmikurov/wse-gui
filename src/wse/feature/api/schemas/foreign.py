"""Foreign discipline schemas."""

from .base import BaseSchema


class WordStudySchema(BaseSchema):
    """Foreign word study schema."""

    definition: str
    explanation: str
