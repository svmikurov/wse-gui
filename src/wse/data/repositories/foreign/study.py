"""Foreign word study repository."""

from dataclasses import dataclass

from injector import inject

from wse.data.sources.foreign.abc import WordStudyPresentationNetworkSourceABC
from wse.feature.api.foreign.schemas import WordStudyPresentationSchema

from . import WordStudyNetworkRepoABC


@inject
@dataclass
class WordsStudyNetworkRepo(WordStudyNetworkRepoABC):
    """Word study network repository."""

    _source: WordStudyPresentationNetworkSourceABC

    def get_data(self) -> WordStudyPresentationSchema:
        """Get word study exercise data."""
        return self._source.fetch_presentation()
