"""Word study progress repo."""

from typing import override

from injector import inject

from wse.data.sources import foreign

from .abc import WordStudyProgressRepoABC


class WordStudyProgressRepo(WordStudyProgressRepoABC):
    """Word study progress repo."""

    @inject
    def __init__(
        self,
        progress_source: foreign.WordStudyProgressNetworkSourceABC,
        case_source: foreign.WordStudyLocaleSourceABC,
    ) -> None:
        """Construct the repo."""
        self._progress_source = progress_source
        self._case_source = case_source

    @override
    def increment(self) -> None:
        """Increment progress of current word study."""
        case_uuid = self._case_source.get_case_uuid()
        self._progress_source.increment_progress(case_uuid)

    @override
    def decrement(self) -> None:
        """Decrement progress of current word study."""
        case_uuid = self._case_source.get_case_uuid()
        self._progress_source.decrement_progress(case_uuid)
