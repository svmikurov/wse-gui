"""Foreign discipline HTTP response schemas."""

from wse.data.sources.foreign import schemas

from ..responses import Response


class WordsResponse(Response):
    """Terms http response schema."""

    data: schemas.WordsData


class WordStudyPresentationResponse(Response):
    """Word study presentation response schema."""

    data: schemas.WordStudyCaseSchema


class WordStudyParamsResponse(Response):
    """Word study params response schema."""

    data: schemas.WordParamsSchema
