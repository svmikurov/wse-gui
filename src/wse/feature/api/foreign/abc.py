"""Abstract base classes for Foreign discipline API."""

from abc import ABC, abstractmethod

from .schemas import (
    WordStudyPresentationParamsSchema,
    WordStudyPresentationSchema,
)


class WordStudyPresentationApiABC(ABC):
    """ABC for Word study presentation API."""

    @abstractmethod
    def fetch_presentation(
        self,
        payload: WordStudyPresentationParamsSchema,
    ) -> WordStudyPresentationSchema:
        """Fetch presentation."""
