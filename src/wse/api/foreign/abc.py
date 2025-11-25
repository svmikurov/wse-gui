"""Abstract base classes for Foreign discipline API."""

from abc import ABC, abstractmethod

from . import requests, schemas


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
        payload: requests.InitialParametersDTO,
    ) -> schemas.PresentationCase:
        """Fetch presentation."""


class WordParamsApiABC(ABC):
    """ABC for Word study params API."""

    @abstractmethod
    def fetch_params(
        self,
    ) -> schemas.PresentationParams:
        """Fetch Word study params."""

    @abstractmethod
    def save_initial_params(
        self,
        data: requests.InitialParametersDTO,
    ) -> None:
        """Save Word study params."""
