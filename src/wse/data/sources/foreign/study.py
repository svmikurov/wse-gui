"""Foreign word study source."""

import logging
from dataclasses import asdict, dataclass
from typing import override

from injector import inject

from wse.api import foreign as api
from wse.data.sources.foreign import schemas

from . import abc as base

log = logging.getLogger(__name__)

DEFAULT_WORD_STUDY_TIMEOUT = 3


@dataclass
class WordStudyLocaleSource:
    """Word study locale source."""


@dataclass(frozen=True)
class WordStudySettingsData:
    """Word study settings Data source."""

    timeout: int = DEFAULT_WORD_STUDY_TIMEOUT


@inject
@dataclass
class WordStudyPresentationNetworkSource(
    base.WordStudyNetworkSourceABC,
):
    """Word study presentation network source."""

    _presentation_api: api.WordStudyPresentationApiABC

    # TODO: Fix payload
    @override
    def fetch_presentation(self) -> schemas.WordStudyCaseSchema:
        """Fetch word study presentation case."""
        params = {'category': None, 'label': None}
        try:
            payload = schemas.WordStudyPresentationParamsSchema.from_dict(
                params
            )
        except Exception as e:
            log.exception(f'Source Network error: {e}')
            raise
        return self._presentation_api.fetch_presentation(payload)


@inject
@dataclass
class WordStudySettingsLocaleSource(base.WordStudySettingsLocaleSourceABC):
    """Word study Locale settings source."""

    _data: WordStudySettingsData

    @override
    def get_settings(self) -> schemas.WordStudySettingsSchema:
        """Get word study settings."""
        try:
            return schemas.WordStudySettingsSchema.from_dict(
                asdict(self._data)
            )
        except Exception as e:
            log.exception(f'Word study Locale settings error: {e}')
            raise
