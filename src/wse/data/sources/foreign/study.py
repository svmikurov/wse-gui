"""Foreign word study source."""

import logging
from dataclasses import asdict, dataclass, replace
from typing import override

from injector import inject

from wse.api import foreign as api
from wse.data.dto import foreign as dto
from wse.data.schemas import foreign as schemas

from . import abc as base

log = logging.getLogger(__name__)

DEFAULT_WORD_STUDY_TIMEOUT = 3


@dataclass(frozen=True)
class WordPresentationData:
    """Word study data."""

    case_uuid: str | None = None
    definition: str | None = None
    explanation: str | None = None
    progress: int | None = None


@inject
@dataclass
class WordPresentationLocaleSource(base.WordPresentationLocaleSourceABC):
    """Word study presentation locale source."""

    _data: WordPresentationData

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
    def get_presentation_data(self) -> schemas.Presentation:
        """Get Presentation part of Word study."""
        if self._data.definition is None or self._data.explanation is None:
            raise RuntimeError('Word study data was not set')
        return schemas.Presentation(
            definition=self._data.definition,
            explanation=self._data.explanation,
            info=schemas.Info(
                progress=self._data.progress,
            ),
        )


@inject
@dataclass
class WordPresentationNetworkSource(
    base.WordPresentationNetworkSourceABC,
):
    """Word study presentation network source."""

    _presentation_api: api.WordPresentationApiABC

    @override
    def fetch_presentation(
        self,
        params: dto.InitialParameters,
    ) -> schemas.PresentationCase:
        """Fetch word study presentation case."""
        try:
            schema = schemas.RequestPresentation.from_dict(asdict(params))
        except Exception as exc:
            log.error(
                f'Request presentation parameters validation error: {str(exc)}'
            )
            raise

        try:
            presentation = self._presentation_api.fetch(schema)
        except Exception as exc:
            log.error(f'Source Network error: {str(exc)}')
            raise
        else:
            return presentation
