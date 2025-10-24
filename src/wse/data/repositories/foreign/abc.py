"""Abstract base classes for Foreign discipline repositories."""

from abc import ABC, abstractmethod
from typing import Any


class WordsStudyNetworkRepoABC(ABC):
    """ABC for Word study network repository."""

    @abstractmethod
    def get_data(self) -> dict[str, Any]:
        """Get word study exercise data."""
