"""Foreign word study repository."""

from dataclasses import dataclass
from typing import Generator

from injector import inject

from wse.config import settings
from wse.utils.loader import load_fixture

from . import WordsStudyNetworkRepoABC

DATA = load_fixture(settings.FIXTURE_PATH / 'words_study.json')


@inject
@dataclass
class WordsStudyNetworkRepo(WordsStudyNetworkRepoABC):
    """Word study network repository."""

    def __post_init__(self) -> None:
        """Construct the repo."""
        self._generator = self._get_generator()

    def _get_generator(self) -> Generator[dict[str, str], None, None]:
        for item in DATA['data']:
            yield item

    def get_data(self) -> dict[str, str]:
        """Get word study exercise data."""
        try:
            return next(self._generator)
        except StopIteration:
            self._generator = self._get_generator()
            return next(self._generator)
