"""Word study progress repo."""

from typing import override

from injector import inject

from wse.data.sources.foreign import WordStudyProgressNetworkSourceABC

from .abc import WordStudyProgressRepoABC


class WordStudyProgressRepo(WordStudyProgressRepoABC):
    """Word study progress repo."""

    @inject
    def __init__(
        self,
        source: WordStudyProgressNetworkSourceABC,
    ) -> None:
        """Construct the repo."""
        self._source = source

    @override
    def increment(self) -> None:
        """Increment progress of current word study."""
        self._source.increment_progress()

    @override
    def decrement(self) -> None:
        """Decrement progress of current word study."""
        self._source.decrement_progress()
