"""Response schema."""

from typing import Literal

from wse.data.schemas.base import BaseSchema
from wse.data.schemas.core import InitialData
from wse.data.schemas.foreign import PresentationCase
from wse.data.schemas.task import Question, Result


class RelatedData(BaseSchema):
    """Response related data schema."""

    balance: str


class Response(BaseSchema):
    """Response schema."""

    status: Literal['success', 'error']
    code: int
    message: str | None
    related_data: RelatedData | None = None

    class Config:
        """Model configuration."""

        extra = 'forbid'


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

    data: PresentationCase
