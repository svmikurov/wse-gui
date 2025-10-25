"""Abstract base classes for Foreign discipline repositories."""

from abc import ABC, abstractmethod

from wse.feature.api.foreign.schemas import WordStudyPresentationSchema


class WordStudyNetworkRepoABC(ABC):
    """ABC for Word study network repository."""

    @abstractmethod
    def get_data(self) -> WordStudyPresentationSchema:
        """Get word study exercise data."""
