"""Abstract base classes for Foreign discipline sources."""

from abc import ABC, abstractmethod

from wse.api.foreign.schemas import WordStudyPresentationSchema


class WordStudyPresentationNetworkSourceABC(
    ABC,
):
    """ABC for Word study presentation network source."""

    @abstractmethod
    def fetch_presentation(self) -> WordStudyPresentationSchema:
        """Fetch word study presentation case."""
