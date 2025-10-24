"""Response schema."""

from typing import Any, Literal

from wse.feature.api.schemas.base import BaseSchema
from wse.feature.api.schemas.core import InitialData
from wse.feature.api.schemas.foreign import WordStudySchema
from wse.feature.api.schemas.task import Question, Result


class RelatedData(BaseSchema):
    """Response related data schema."""

    balance: str


class Response(BaseSchema):
    """Response schema."""

    status: Literal['success', 'error']
    message: str | None
    related_data: RelatedData | None = None


class ItemsData(BaseSchema):
    """Response items data."""

    count: int
    next: str | None
    previous: str | None
    results: list[Any]


class QuestionResponse(Response):
    """Response with task question schema."""

    data: Question


class ResultResponse(Response):
    """Response with task checking response schema."""

    data: Result


class InitialDataResponse(BaseSchema):
    """Initial data response schema."""

    # Temporary balance
    data: InitialData


# Foreign discipline
# ------------------


class WordStudyResponse(Response):
    """Response with word."""

    data: WordStudySchema
