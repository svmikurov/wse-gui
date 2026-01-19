"""Presentation api test cases."""

from typing import Literal, TypedDict

# TODO: Update types
# Types are currently used to create fixtures.
# Replace with project types.

# Case type question
# ------------------


# Response data types


class RelatedDict(TypedDict):
    """Response related data typed dict."""

    balance: str


class PresentationInfoDict(TypedDict):
    """Presentation case info typed dict."""

    progress: int


class PresentationCaseDict(TypedDict):
    """Presentation case typed dict."""

    case_uuid: str
    question: str
    answer: str
    info: PresentationInfoDict


class ResponseDict(TypedDict):
    """Presentation response typed dict."""

    status: Literal['success', 'error']
    code: int
    message: str | None
    related_data: RelatedDict
    data: PresentationCaseDict


# Cases
# -----


VALID_RESPONSE_PAYLOAD = ResponseDict(
    status='success',
    message='Some message',
    code=200,
    related_data=RelatedDict(
        balance='12',
    ),
    data=PresentationCaseDict(
        case_uuid='5b518a3e-45a4-4147-a097-0ed28211d8a4',
        question='test',
        answer='тест',
        info=PresentationInfoDict(
            progress=8,
        ),
    ),
)
