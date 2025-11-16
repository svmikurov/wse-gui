"""Abstract base classes for Foreign discipline API."""

import uuid
from abc import ABC, abstractmethod

from wse.data.sources.foreign import schemas


class WordStudyProgressApiABC(ABC):
    """ABC for Word study progress API."""

    @abstractmethod
    def increment_progress(self, case_uuid: uuid.UUID) -> None:
        """Send API request to increment Word study progress."""

    @abstractmethod
    def decrement_progress(self, case_uuid: uuid.UUID) -> None:
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
    ) -> schemas.ParamsChoices:
        """Fetch Word study params."""
