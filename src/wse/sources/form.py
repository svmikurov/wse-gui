"""Form sources."""

from toga.sources import Source


class WordForm:
    """A class to wrap individual word."""

    def __init__(
        self,
        word_id: int,
        foreign_word: str,
        native_word: str,
    ) -> None:
        """Construct the word wrap."""
        self.word_id = word_id
        self.foreign_word = foreign_word
        self.native_word = native_word


class WordFormSource(Source):
    """Custom word form source."""

    def __init__(self) -> None:
        """Construct the source."""
        super().__init__()
