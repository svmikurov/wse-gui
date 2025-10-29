"""Foreign discipline HTTP response schemas."""

from datetime import datetime

from ....api.schemas.base import BaseSchema, ItemsData

# TODO: Refactor, now to many schemas

# Nested schemas
# --------------


class IdNameSchema(BaseSchema):
    """Dict representation of entity only with its 'name' and 'ID'."""

    id: int
    name: str


class WordSchema(BaseSchema):
    """Word entity."""

    id: str
    definition: str
    explanation: str
    created_at: datetime


class WordsData(ItemsData):
    """Words data schema."""

    results: list[WordSchema]


# Word study
# ----------


class WordStudyPresentationParamsSchema(BaseSchema):
    """Word study presentation schema for HTTP request."""

    category: IdNameSchema | None
    label: IdNameSchema | None

    class Config:
        """Schema configuration."""

        extra = 'forbid'


class WordStudyPresentationSchema(BaseSchema):
    """Word study presentation schema for HTTP response."""

    definition: str
    explanation: str


# Word study settings
# -------------------


class WordStudySettingsSchema(BaseSchema):
    """Word study settings schema."""

    timeout: int


# Word study params
# -----------------


class WordDefaultSchema(BaseSchema):
    """Default Word study case schema."""

    default_category: IdNameSchema | None
    default_label: IdNameSchema | None


class WordSelectedSchema(BaseSchema):
    """Selected Word study case schema."""

    # The field may not be selected.
    selected_category: IdNameSchema | None
    selected_label: IdNameSchema | None


class WordParamsSchema(
    WordDefaultSchema,
):
    """Word study params schema."""

    categories: list[IdNameSchema]
    labels: list[IdNameSchema]
