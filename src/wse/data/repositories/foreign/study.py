"""Foreign word study repository."""

from dataclasses import dataclass
from typing import override

from injector import inject

from wse.data.sources import foreign as source
from wse.data.sources.foreign import schemas

from . import (
    WordStudyCaseRepoABC,
    WordStudySettingsRepoABC,
)


@inject
@dataclass
class WordStudyCaseRepo(WordStudyCaseRepoABC):
    """Word study network repository."""

    _network_source: source.WordStudyNetworkSourceABC
    _locale_source: source.WordStudyLocaleSourceABC

    @override
    def get_word(self) -> schemas.WordPresentationSchema:
        """Get word to study."""
        case = self._network_source.fetch_presentation()
        self._locale_source.set_case(case)
        return self._locale_source.get_presentation_data()


@inject
@dataclass
class WordStudySettingsRepo(WordStudySettingsRepoABC):
    """Word study settings repository."""

    _source: source.WordStudySettingsLocaleSourceABC

    @override
    def get_settings(self) -> schemas.WordStudySettingsSchema:
        """Get word study settings."""
        return self._source.get_settings()
