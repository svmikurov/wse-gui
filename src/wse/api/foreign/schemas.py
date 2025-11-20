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


class ParamsChoices(base.BaseSchema):
    """Schema representing a case params choices."""

    categories: list[base.IdNameSchema] = []
    labels: list[base.IdNameSchema] | None


# Rename to `InitialParams`
class InitialChoice(base.BaseSchema):
    """Schema representing an initial params choice."""

    category: base.IdNameSchema | None
    label: base.IdNameSchema | None


class PresentationSettings(base.BaseSchema):
    """Schema representing a settings schema."""

    question_timeout: float | None = 1.5
    answer_timeout: float | None = 1.5


class PresentationParams(
    ParamsChoices,
    InitialChoice,
    PresentationSettings,
):
    """Default Presentation params with choices."""
