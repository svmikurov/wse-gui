"""Foreign discipline HTTP response schemas."""

from wse.core.api.response import Response

from ...data.sources.foreign.schemas import (
    WordParamsSchema,
    WordsData,
    WordStudyCaseSchema,
)


class WordsResponse(Response):
    """Terms http response schema."""

    data: WordsData


class WordStudyPresentationResponse(Response):
    """Word study presentation response schema."""

    data: WordStudyCaseSchema


class WordStudyParamsResponse(Response):
    """Word study params response schema."""

    data: WordParamsSchema
