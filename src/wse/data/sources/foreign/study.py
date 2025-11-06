"""Foreign word study source."""

import logging
from dataclasses import asdict, dataclass
from typing import override

from injector import inject

from wse.api.foreign.abc import WordStudyPresentationApiABC
from wse.data.sources.foreign.schemas import (
    WordStudyCaseSchema,
    WordStudyPresentationParamsSchema,
    WordStudySettingsSchema,
)

from .abc import (
    WordStudyNetworkSourceABC,
    WordStudySettingsLocaleSourceABC,
)

log = logging.getLogger(__name__)

DEFAULT_WORD_STUDY_TIMEOUT = 3


@dataclass(frozen=True)
class WordStudySettingsData:
    """Word study settings Data source."""

    timeout: int = DEFAULT_WORD_STUDY_TIMEOUT


@inject
@dataclass
class WordStudyPresentationNetworkSource(
    WordStudyNetworkSourceABC,
):
    """Word study presentation network source."""

    _presentation_api: WordStudyPresentationApiABC

    # TODO: Fix payload
    @override
    def fetch_presentation(self) -> WordStudyCaseSchema:
        """Fetch word study presentation case."""
        params = {'category': None, 'label': None}
        try:
            payload = WordStudyPresentationParamsSchema.from_dict(params)
        except Exception as e:
            log.exception(f'Source Network error: {e}')
            raise
        return self._presentation_api.fetch_presentation(payload)


@inject
@dataclass
class WordStudySettingsLocaleSource(WordStudySettingsLocaleSourceABC):
    """Word study Locale settings source."""

    _data: WordStudySettingsData

    @override
    def get_settings(self) -> WordStudySettingsSchema:
        """Get word study settings."""
        try:
            return WordStudySettingsSchema.from_dict(asdict(self._data))
        except Exception as e:
            log.exception(f'Word study Locale settings error: {e}')
            raise
