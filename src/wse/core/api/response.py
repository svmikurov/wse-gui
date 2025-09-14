"""Response schema."""

from typing import Literal

from wse.feature.base import BaseSchema
from wse.feature.services import Question, Result
from wse.feature.shared.schemas.core import InitialData


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
