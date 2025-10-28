"""Foreign word study repository."""

from dataclasses import dataclass

from injector import inject

from wse.data.sources.foreign.abc import WordStudyPresentationNetworkSourceABC
from wse.data.sources.foreign.schemas import WordStudyPresentationSchema

from . import GetWordStudyRepoABC


@inject
@dataclass
class GetWordStudyRepo(GetWordStudyRepoABC):
    """Word study network repository."""

    _source: WordStudyPresentationNetworkSourceABC

    def get_word(self) -> WordStudyPresentationSchema:
        """Get word to study."""
        return self._source.fetch_presentation()
