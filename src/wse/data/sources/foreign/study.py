"""Foreign word study source."""

import logging
import uuid
from dataclasses import asdict, dataclass, replace
from typing import override

from injector import inject

from wse.api import foreign as api
from wse.data.sources.foreign import schemas

from . import abc as base

log = logging.getLogger(__name__)

DEFAULT_WORD_STUDY_TIMEOUT = 3


@dataclass(frozen=True)
class WordStudyData:
    """Word study data."""

    case_uuid: uuid.UUID | None = None
    definition: str | None = None
    explanation: str | None = None


class WordStudyLocaleSource(base.WordStudyLocaleSourceABC):
    """Word study locale source."""

    @inject
    def __init__(
        self,
        data: WordStudyData,
    ) -> None:
        """Construct the source."""
        self._data = data

    @override
    def set_case(self, case: schemas.WordStudyCaseSchema) -> None:
        """Set Word study case."""
        self._data = replace(self._data, **case.to_dict())

    @override
    def get_case_uuid(self) -> uuid.UUID:
        """Get case UUID."""
        if self._data.case_uuid is None:
            raise RuntimeError('Word study data was not set')
        return self._data.case_uuid

    @override
    def get_presentation_data(self) -> schemas.WordPresentationSchema:
        """Get Presentation part of Word study."""
        if self._data.definition is None or self._data.explanation is None:
            raise RuntimeError('Word study data was not set')
        return schemas.WordPresentationSchema(
            definition=self._data.definition,
            explanation=self._data.explanation,
        )


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
            presentation = self._presentation_api.fetch_presentation(payload)
        except Exception as e:
            log.exception(f'Source Network error: {e}')
            raise
        else:
            return presentation


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
