"""Word study Presentation repository."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING, override

from injector import inject

from wse.data.repos import foreign as repos
from wse.data.sources import foreign as sources

if TYPE_CHECKING:
    from wse.data.schemas import foreign as schemas

logger = logging.getLogger(__name__)


@inject
@dataclass
class WordPresentationRepo(repos.WordPresentationRepoABC):
    """Word study Presentation repository."""

    _locale_source: sources.WordPresentationLocaleSourceABC
    _network_source: sources.WordPresentationNetworkSourceABC
    _params_repo: repos.WordParametersRepoABC

    @override
    def get_word(self) -> schemas.Presentation:
        """Get Word study presentation data."""
        try:
            params = self._params_repo.get()
        except Exception as exc:
            logger.error(f'Get presentation parameters error: {exc}')
            raise

        try:
            case = self._network_source.fetch_presentation(params)
        except Exception as exc:
            logger.error(f'Get a remote presentation data error: {exc}')
            raise

        try:
            self._locale_source.set_case(case)
        except Exception as exc:
            logger.error(f'Set presentation data locally error: {exc}')
            raise

        try:
            return self._locale_source.get_presentation_data()
        except Exception as exc:
            logger.error(f'Get locally saved presentation data error: {exc}')
            raise
