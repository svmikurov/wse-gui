"""Foreign word study source."""

from dataclasses import dataclass

from injector import inject

from wse.api.foreign.abc import WordStudyPresentationApiABC
from wse.api.foreign.schemas import (
    WordStudyPresentationParamsSchema,
    WordStudyPresentationSchema,
)

from .abc import WordStudyPresentationNetworkSourceABC


@inject
@dataclass
class WordStudyPresentationNetworkSource(
    WordStudyPresentationNetworkSourceABC,
):
    """Word study presentation network source."""

    _presentation_api: WordStudyPresentationApiABC

    # TODO: Fix payload
    def fetch_presentation(self) -> WordStudyPresentationSchema:
        """Fetch word study presentation case."""
        params = {'category': None, 'marks': None}
        payload = WordStudyPresentationParamsSchema.from_dict(params)
        return self._presentation_api.fetch_presentation(payload)
