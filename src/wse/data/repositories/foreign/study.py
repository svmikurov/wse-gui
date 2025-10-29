"""Foreign word study repository."""

from dataclasses import dataclass
from typing import override

from injector import inject

from wse.data.sources.foreign.abc import (
    WordStudyPresentationNetworkSourceABC,
    WordStudySettingsLocaleSourceABC,
)
from wse.data.sources.foreign.schemas import (
    WordStudyPresentationSchema,
    WordStudySettingsSchema,
)

from . import (
    GetWordStudyRepoABC,
    WordStudySettingsRepoABC,
)


@inject
@dataclass
class GetWordStudyRepo(GetWordStudyRepoABC):
    """Word study network repository."""

    _source: WordStudyPresentationNetworkSourceABC

    @override
    def get_word(self) -> WordStudyPresentationSchema:
        """Get word to study."""
        return self._source.fetch_presentation()


@inject
@dataclass
class WordStudySettingsRepo(WordStudySettingsRepoABC):
    """Word study settings repository."""

    _source: WordStudySettingsLocaleSourceABC

    @override
    def get_settings(self) -> WordStudySettingsSchema:
        """Get word study settings."""
        return self._source.get_settings()
