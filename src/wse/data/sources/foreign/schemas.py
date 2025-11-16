"""Foreign discipline HTTP response schemas."""

import uuid
from datetime import datetime

from wse.api.schemas import base

# TODO: Refactor, now to many schemas

# Nested schemas
# --------------


class WordSchema(base.BaseSchema):
    """Word entity."""

    id: str
    definition: str
    explanation: str
    created_at: datetime


class WordsData(base.ItemsData):
    """Words data schema."""

    results: list[WordSchema]


# Word study
# ----------


class WordStudyPresentationParamsSchema(base.BaseSchema):
    """Word study presentation schema for HTTP request."""

    category: base.IdNameSchema | None
    label: base.IdNameSchema | None

    class Config:
        """Schema configuration."""

        extra = 'forbid'


class WordPresentationSchema(base.BaseSchema):
    """Presentation part of Word study schema."""

    definition: str
    explanation: str


class WordStudyCaseSchema(WordPresentationSchema):
    """Word study case schema."""

    case_uuid: uuid.UUID


# Word study settings
# -------------------


class WordStudySettingsSchema(base.BaseSchema):
    """Word study settings schema."""

    question_timeout: float = 1.5
    answer_timeout: float = 1.5


# Word study params
# -----------------


class WordDefaultSchema(base.BaseSchema):
    """Default Word study case schema."""

    default_category: base.IdNameSchema | None
    default_label: base.IdNameSchema | None


class WordSelectedSchema(base.BaseSchema):
    """Selected Word study case schema."""

    selected_category: base.IdNameSchema | None
    selected_label: base.IdNameSchema | None


class WordParamsSchema(
    WordDefaultSchema,
):
    """Word study params schema."""

    categories: list[base.IdNameSchema]
    labels: list[base.IdNameSchema]
