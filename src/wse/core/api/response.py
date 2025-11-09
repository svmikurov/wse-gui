"""Response schema."""

from typing import Literal

from wse.api.schemas.base import BaseSchema
from wse.api.schemas.core import InitialData
from wse.api.schemas.task import Question, Result
from wse.data.sources.foreign.schemas import WordStudyCaseSchema


class RelatedData(BaseSchema):
    """Response related data schema."""

    balance: str


class Response(BaseSchema):
    """Response schema."""

    status: Literal['success', 'error']
    message: str | None
    related_data: RelatedData | None = None


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

    data: WordStudyCaseSchema
