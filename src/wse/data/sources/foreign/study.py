"""Foreign word study source."""

import logging
from dataclasses import dataclass

from injector import inject

from wse.api.foreign.abc import WordStudyPresentationApiABC
from wse.data.sources.foreign.schemas import (
    WordStudyPresentationParamsSchema,
    WordStudyPresentationSchema,
)

from .abc import WordStudyPresentationNetworkSourceABC

log = logging.getLogger(__name__)


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
        params = {'category': None, 'label': None}
        try:
            payload = WordStudyPresentationParamsSchema.from_dict(params)
        except Exception as e:
            log.exception(f'Source Network error: {e}')
            raise
        return self._presentation_api.fetch_presentation(payload)
