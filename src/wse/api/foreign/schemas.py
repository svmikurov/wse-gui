"""Foreign discipline HTTP response schemas."""

from datetime import datetime

from wse.api.schemas import base

# TODO: Refactor, now to many schemas

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


# Presentation case
# -----------------


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


# Presentation params
# -------------------


class PresentationParams(base.BaseSchema):
    """Presentation params for case request."""

    category: base.IdNameSchema | None
    label: base.IdNameSchema | None

    class Config:
        """Schema configuration."""

        extra = 'forbid'


class InitialParams(base.BaseSchema):
    """Schema representing a initial params."""

    category: base.IdNameSchema | None
    label: base.IdNameSchema | None


class SelectedParams(base.BaseSchema):
    """Presentation case selected params."""

    selected_category: base.IdNameSchema | None
    selected_label: base.IdNameSchema | None


class ParamsChoices(base.BaseSchema):
    """Presentation case params choices."""

    categories: list[base.IdNameSchema]
    labels: list[base.IdNameSchema]


class ParamsSchema(
    InitialParams,
    ParamsChoices,
):
    """Default Presentation params with choices."""


# Presentation settings
# ---------------------


class PresentationSettings(base.BaseSchema):
    """Word study settings schema."""

    question_timeout: float = 1.5
    answer_timeout: float = 1.5
