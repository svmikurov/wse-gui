"""Foreign discipline schemas."""

from datetime import datetime

from pydantic import Field

from wse.data.dto import foreign as dto
from wse.data.schemas import base

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


# Word study case
# ---------------


class Info(base.BaseSchema):
    """Schema representing an exercise info."""

    progress: int | None


class Presentation(base.BaseSchema):
    """Schema representing a Presentation exercise."""

    question: str
    answer: str
    info: Info | None = None


class PresentationCase(Presentation):
    """Schema representing a Presentation case."""

    case_uuid: str


# Word study parameters
# ---------------------


class PresentationOptions(base.BaseSchema):
    """Word study options schema."""

    categories: list[base.IdName] = []
    marks: list[base.IdName] = []
    sources: list[base.IdName] = []
    periods: list[base.IdName] = []
    translation_orders: list[base.CodeName] = []


class SelectedParameters(base.BaseSchema):
    """Word study selected parameters schema."""

    category: base.IdName | None
    mark: list[base.IdName] = Field(
        description='The field has a many-to-many relationship'
    )
    word_source: base.IdName | None
    translation_order: base.CodeName | None
    start_period: base.IdName | None
    end_period: base.IdName | None


class SetPresentation(base.BaseSchema):
    """Word study set parameters schema."""

    word_count: int | None

    is_study: bool | None
    is_repeat: bool | None
    is_examine: bool | None
    is_know: bool | None


class PresentationSettings(base.BaseSchema):
    """Word study Presentation settings schema."""

    question_timeout: int | None = 2
    answer_timeout: int | None = 2


class InitialParameters(
    SelectedParameters,
    SetPresentation,
    PresentationSettings,
):
    """Schema representing an update presentation parameters."""


class RequestPresentation(
    SelectedParameters,
    SetPresentation,
):
    """Schema representing a request presentation parameters."""


class PresentationParameters(
    PresentationOptions,
    SelectedParameters,
    SetPresentation,
    PresentationSettings,
):
    """Default Presentation parameters with choices."""

    def to_dto(self) -> dto.PresentationParameters:
        """Convert Word study Presentation parameters schema to DTO."""
        attrs = {}

        for field, value in self:
            if value is None:
                continue

            elif isinstance(value, int):
                attrs[field] = value

            else:
                attrs[field] = self._convert_nested(value)  # type: ignore[assignment]

        return dto.PresentationParameters(**attrs)  # type: ignore[arg-type]

    def _convert_nested(self, value: base.WordOptions) -> dto.WordOptions:
        """Convert nested schema to DTO."""
        match value:
            case base.IdName(id=id, name=name):
                return dto.IdName(id, name)

            case base.CodeName(code=code, name=name):
                return dto.CodeName(code, name)

            case list(items):
                return [self._convert_nested(item) for item in items]  # type: ignore[return-value]

            case _:
                raise TypeError(f'Unsupported type: {type(value).__name__}')
