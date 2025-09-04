"""Response schema."""

from typing import Literal

from wse.feature.base import BaseSchema
from wse.feature.services import Question, Result


class RelatedData(BaseSchema):
    """Response related data."""

    balance: str


class Response(BaseSchema):
    """Response schema."""

    status: Literal['success', 'error']
    message: str | None
    related_data: RelatedData | None = None


class QuestionResponse(Response):
    """Response with task question."""

    data: Question


class ResultResponse(Response):
    """Response with task checking response."""

    data: Result
