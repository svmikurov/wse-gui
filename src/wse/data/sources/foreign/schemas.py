"""Foreign discipline HTTP response schemas."""

import uuid
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
    """Presentation exercise additional info."""

    progress: int


class PresentationSchema(base.BaseSchema):
    """Presentation exercise schema."""

    definition: str
    explanation: str
    info: Info | None = None


class PresentationCase(PresentationSchema):
    """Presentation case schema."""

    case_uuid: uuid.UUID


# Presentation params
# -------------------


class PresentationParams(base.BaseSchema):
    """Word study Presentation request params."""

    category: base.IdNameSchema | None
    label: base.IdNameSchema | None

    class Config:
        """Schema configuration."""

        extra = 'forbid'


class DefaultParams(base.BaseSchema):
    """Presentation case default params."""

    default_category: base.IdNameSchema | None
    default_label: base.IdNameSchema | None


class SelectedParams(base.BaseSchema):
    """Presentation case selected params."""

    selected_category: base.IdNameSchema | None
    selected_label: base.IdNameSchema | None


class ParamsChoices(base.BaseSchema):
    """Presentation case params choices."""

    categories: list[base.IdNameSchema]
    labels: list[base.IdNameSchema]


class ParamsSchema(
    DefaultParams,
    ParamsChoices,
):
    """Presentation params schema."""


# Presentation settings
# ---------------------


class PresentationSettings(base.BaseSchema):
    """Word study settings schema."""

    question_timeout: float = 1.5
    answer_timeout: float = 1.5
