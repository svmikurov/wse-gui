"""Foreign discipline HTTP response schemas."""

from wse.data.sources.foreign import schemas

from ..responses import Response


class WordsResponse(Response):
    """Terms http response schema."""

    data: schemas.Words


class WordStudyPresentationResponse(Response):
    """Word study presentation response schema."""

    data: schemas.PresentationCase


class WordStudyParamsResponse(Response):
    """Word study params response schema."""

    data: schemas.ParamsSchema
