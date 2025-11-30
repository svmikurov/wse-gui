"""Foreign discipline HTTP response schemas."""

from datetime import datetime
from typing import TypeAlias

from wse.data.dto import params as dto
from wse.data.schemas import base

OptionsSchemas: TypeAlias = (
    base.IdNameSchema
    | base.CodeNameSchema
    | list[base.IdNameSchema]
    | list[base.CodeNameSchema]
)
OptionsDTOs: TypeAlias = (
    dto.IdName | dto.CodeName | list[dto.IdName] | list[dto.CodeName]
)

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


# Word study Presentation parameters
# ----------------------------------


class PresentationOptionsSchema(base.BaseSchema):
    """Word study options schema."""

    categories: list[base.IdNameSchema] = []
    marks: list[base.IdNameSchema] = []
    sources: list[base.IdNameSchema] = []
    periods: list[base.IdNameSchema] = []
    translation_orders: list[base.CodeNameSchema] = []


class SelectedParametersSchema(base.BaseSchema):
    """Word study selected parameters schema."""

    category: base.IdNameSchema | None
    mark: base.IdNameSchema | None
    word_source: base.IdNameSchema | None
    translation_order: base.CodeNameSchema | None
    start_period: base.IdNameSchema | None
    end_period: base.IdNameSchema | None


class PresentationSettingsSchema(base.BaseSchema):
    """Word study settings schema."""

    word_count: int | None
    question_timeout: int | None = 2
    answer_timeout: int | None = 2


class InitialParametersSchema(
    SelectedParametersSchema,
    PresentationSettingsSchema,
):
    """Schema representing an update presentation parameters."""


class PresentationParametersSchema(
    PresentationOptionsSchema,
    SelectedParametersSchema,
    PresentationSettingsSchema,
):
    """Default Presentation parameters with choices."""

    def to_dto(self) -> dto.PresentationParametersDTO:
        """Convert Word study Presentation parameters schema to DTO."""
        attrs = {}

        for field, value in self:
            if not value or isinstance(value, int):
                attrs[field] = value
            else:
                attrs[field] = self._convert_nested(value)

        return dto.PresentationParametersDTO(**attrs)  # type: ignore[arg-type]

    def _convert_nested(self, value: OptionsSchemas) -> OptionsDTOs:
        """Convert nested schema to DTO."""
        match value:
            case base.IdNameSchema(id=id, name=name):
                return dto.IdName(id, name)

            case base.CodeNameSchema(code=code, name=name):
                return dto.CodeName(code, name)

            case list(items):
                return [self._convert_nested(item) for item in items]  # type: ignore[return-value]

            case _:
                raise TypeError(f'Got unexpected type: {type(value).__name__}')
