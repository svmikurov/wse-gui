"""Defines task conditions."""


class Answer:
    """The task answer."""

    def __init__(self, text: str) -> None:
        """Construct the answer."""
        self._text = text

    @property
    def text(self) -> str:
        """Return a string representation of the answer."""
        return self._text
