"""Abstract base classes for text handlers."""

from abc import ABC, abstractmethod


class TextHyphenationABC(ABC):
    """ABC for text hyphenation."""

    @classmethod
    @abstractmethod
    def adapt(cls, text: str) -> str:
        """Adapt text for screen."""
