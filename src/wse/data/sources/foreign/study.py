"""Foreign word study source."""

import logging
from dataclasses import dataclass, replace
from typing import override

from injector import inject

from wse.api import foreign as api
from wse.api.foreign import requests, schemas

from . import abc as base

log = logging.getLogger(__name__)

DEFAULT_WORD_STUDY_TIMEOUT = 3


@dataclass(frozen=True)
class WordStudyData:
    """Word study data."""

    case_uuid: str | None = None
    definition: str | None = None
    explanation: str | None = None
    progress: int | None = None


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
    def set_case(self, case: schemas.PresentationCase) -> None:
        """Set Word study case."""
        # TODO: Refactor
        self._data = replace(
            self._data,
            case_uuid=case.case_uuid,
            definition=case.definition,
            explanation=case.explanation,
            progress=case.info.progress if case.info else None,
        )

    @override
    def get_case_uuid(self) -> str:
        """Get case UUID."""
        if self._data.case_uuid is None:
            raise RuntimeError('Word study data was not set')
        return self._data.case_uuid

    @override
    def get_presentation_data(self) -> schemas.PresentationSchema:
        """Get Presentation part of Word study."""
        if self._data.definition is None or self._data.explanation is None:
            raise RuntimeError('Word study data was not set')
        return schemas.PresentationSchema(
            definition=self._data.definition,
            explanation=self._data.explanation,
            info=schemas.Info(
                progress=self._data.progress,
            ),
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

    @override
    def fetch_presentation(
        self,
        params: requests.InitialParams,
    ) -> schemas.PresentationCase:
        """Fetch word study presentation case."""
        try:
            presentation = self._presentation_api.fetch_presentation(params)
        except Exception as exc:
            log.error(f'Source Network error: {str(exc)}')
            raise
        else:
            return presentation
