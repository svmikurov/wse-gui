"""Foreign discipline HTTP response schemas."""

from wse.data.schemas import foreign as schemas

from ..responses import Response


class WordsResponse(Response):
    """Terms http response schema."""

    data: schemas.Words


class WordStudyPresentationResponse(Response):
    """Word study presentation response schema."""

    data: schemas.PresentationCase | None


class WordStudyParametersResponse(Response):
    """Word study params response schema."""

    data: schemas.PresentationParameters
