"""Abstract base classes for Foreign discipline API clients."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from wse.data.schemas import foreign as schemas


class UpdateProgressPayload(TypedDict):
    """Update progress payload types."""

    case_uuid: str
    is_known: bool


class WordProgressApiABC(ABC):
    """ABC for Word study progress API client."""

    @abstractmethod
    def update(self, payload: UpdateProgressPayload) -> None:
        """Update Word study progress."""


class WordPresentationApiABC(ABC):
    """ABC for Word study presentation API client."""

    @abstractmethod
    def fetch(
        self,
        payload: schemas.RequestPresentation,
    ) -> schemas.PresentationCase:
        """Fetch Word study presentation."""


class WordParametersApiABC(ABC):
    """ABC for Word study parameters API client."""

    @abstractmethod
    def fetch(self) -> schemas.PresentationParameters:
        """Fetch Word study parameters."""

    @abstractmethod
    def save(
        self,
        data: schemas.InitialParameters,
    ) -> schemas.PresentationParameters:
        """Save Word study parameters."""
