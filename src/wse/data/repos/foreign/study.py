"""Word study Presentation repository."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, override

from injector import inject

from wse.data.repos import foreign as repos
from wse.data.sources import foreign as sources

if TYPE_CHECKING:
    from wse.data.schemas import foreign as schemas


@inject
@dataclass
class WordPresentationRepo(repos.WordPresentationRepoABC):
    """Word study Presentation repository."""

    _locale_source: sources.WordPresentationLocaleSourceABC
    _network_source: sources.WordPresentationNetworkSourceABC
    _params_repo: repos.WordParametersRepoABC

    @override
    def get_word(self) -> schemas.Presentation:
        """Get Word study schema."""
        params = self._params_repo.get()
        case = self._network_source.fetch_presentation(params)
        self._locale_source.set_case(case)
        return self._locale_source.get_presentation_data()
