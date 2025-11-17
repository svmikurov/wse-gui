"""Abstract base classes for Foreign discipline API."""

from abc import ABC, abstractmethod

from wse.data.sources.foreign import schemas


class WordStudyProgressApiABC(ABC):
    """ABC for Word study progress API."""

    @abstractmethod
    def increment_progress(self, case_uuid: str) -> None:
        """Send API request to increment Word study progress."""

    @abstractmethod
    def decrement_progress(self, case_uuid: str) -> None:
        """Send API request to decrement Word study progress."""


class WordStudyPresentationApiABC(ABC):
    """ABC for Word study presentation API."""

    @abstractmethod
    def fetch_presentation(
        self,
        payload: schemas.PresentationParams,
    ) -> schemas.PresentationCase:
        """Fetch presentation."""


class WordParamsApiABC(ABC):
    """ABC for Word study params API."""

    @abstractmethod
    def fetch_initial_params(
        self,
    ) -> schemas.ParamsSchema:
        """Fetch Word study params."""
