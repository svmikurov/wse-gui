"""Foreign discipline HTTP response schemas."""

from datetime import datetime

from wse.api.schemas import base

# Word schema
# -----------


class Word(base.BaseSchema):
    """Word schema."""

    id: str
    definition: str
    explanation: str
    created_at: datetime


class Words(base.ItemsData):
    """Words schema."""

    results: list[Word]


# Word study Presentation case
# ----------------------------


class Info(base.BaseSchema):
    """Schema representing an exercise info."""

    progress: int | None


class PresentationSchema(base.BaseSchema):
    """Schema representing a Presentation exercise."""

    definition: str
    explanation: str
    info: Info | None = None


class PresentationCase(PresentationSchema):
    """Schema representing a Presentation case."""

    case_uuid: str


# Word study Presentation params
# ------------------------------


class ParamOptions(base.BaseSchema):
    """Schema representing a case params choices."""

    categories: list[base.IdNameSchema] = []
    marks: list[base.IdNameSchema] = []
    sources: list[base.IdNameSchema] = []
    periods: list[base.IdNameSchema] = []
    translation_orders: list[base.CodeNameSchema] = []


class InitialChoices(base.BaseSchema):
    """Schema representing an initial params choice."""

    category: base.IdNameSchema | None
    mark: base.IdNameSchema | None
    word_source: base.IdNameSchema | None
    translation_order: base.CodeNameSchema | None
    start_period: base.IdNameSchema | None
    end_period: base.IdNameSchema | None


class PresentationSettings(base.BaseSchema):
    """Schema representing a settings schema."""

    word_count: int | None
    question_timeout: int | None = 2
    answer_timeout: int | None = 2


class PresentationParams(
    ParamOptions,
    InitialChoices,
    PresentationSettings,
):
    """Default Presentation params with choices."""
