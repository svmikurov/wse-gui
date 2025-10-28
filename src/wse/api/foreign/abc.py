"""Abstract base classes for Foreign discipline API."""

from abc import ABC, abstractmethod

from ...data.sources.foreign.schemas import (
    WordParamsSchema,
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


class WordParamsApiABC(ABC):
    """ABC for Word study params API."""

    @abstractmethod
    def fetch_initial_params(
        self,
    ) -> WordParamsSchema:
        """Fetch Word study params."""
