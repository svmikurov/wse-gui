"""Foreign discipline HTTP response schemas."""

from datetime import datetime

from ..schemas.base import BaseSchema, ItemsData


class WordSchema(BaseSchema):
    """Word entity."""

    id: str
    definition: str
    explanation: str
    created_at: datetime


class WordsData(ItemsData):
    """Words data schema."""

    results: list[WordSchema]


class WordStudyPresentationParamsSchema(BaseSchema):
    """Word study presentation schema for HTTP request."""

    category: list[str] | None
    marks: list[str] | None

    class Config:
        """Schema configuration."""

        extra = 'forbid'


class WordStudyPresentationSchema(BaseSchema):
    """Word study presentation schema for HTTP response."""

    definition: str
    explanation: str
