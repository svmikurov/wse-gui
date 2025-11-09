"""Foreign word study repository."""

from dataclasses import dataclass
from typing import override

from injector import inject

from wse.data.sources import foreign as sources
from wse.data.sources.foreign import schema

from . import (
    WordStudyRepoABC,
    WordStudySettingsRepoABC,
)


@inject
@dataclass
class WordStudyRepo(WordStudyRepoABC):
    """Word study repository."""

    _locale_source: sources.WordStudyLocaleSourceABC
    _network_source: sources.WordStudyNetworkSourceABC

    @override
    def get_word(self) -> schema.WordPresentationSchema:
        """Get word to study."""
        try:
            case = self._network_source.fetch_presentation()
        except Exception:
            raise
        self._locale_source.set_case(case)
        return self._locale_source.get_presentation_data()


@inject
@dataclass
class WordStudySettingsRepo(WordStudySettingsRepoABC):
    """Word study settings repository."""

    _source: sources.WordStudySettingsLocaleSourceABC

    @override
    def get_settings(self) -> schema.WordStudySettingsSchema:
        """Get word study settings."""
        return self._source.get_settings()
