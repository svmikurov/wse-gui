"""Foreign discipline HTTP response schemas."""

from wse.core.api.response import Response

from .schemas import WordsData, WordStudyPresentationSchema


class WordsResponse(Response):
    """Terms http response schema."""

    data: WordsData


class WordStudyPresentationResponse(Response):
    """Word study presentation response schema."""

    data: WordStudyPresentationSchema
