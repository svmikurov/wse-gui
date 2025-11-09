"""Abstract base classes for Foreign discipline sources."""

import uuid
from abc import ABC, abstractmethod
from typing import Literal

from wse.data.sources.foreign import schemas
from wse.feature.observer.generic import ObserverManagerGenABC

# Word study settings
# -------------------


class WordStudySettingsLocaleSourceABC(ABC):
    """Word study Locale settings source."""

    @abstractmethod
    def get_settings(self) -> schemas.WordStudySettingsSchema:
        """Get Word study settings."""


# Word study source
# -----------------


class WordStudyLocaleSourceABC(ABC):
    """Word study locale source."""

    @abstractmethod
    def set_case(self, case: schemas.WordStudyCaseSchema) -> None:
        """Set Word study case."""

    @abstractmethod
    def get_case_uuid(self) -> uuid.UUID:
        """Get case UUID."""

    @abstractmethod
    def get_presentation_data(self) -> schemas.WordPresentationSchema:
        """Get Presentation part of Word study."""


class WordStudyProgressNetworkSourceABC(ABC):
    """Word study progress Network Source."""

    @abstractmethod
    def increment_progress(self, case_uuid: uuid.UUID) -> None:
        """Increment Word study progress."""

    @abstractmethod
    def decrement_progress(self, case_uuid: uuid.UUID) -> None:
        """Decrement Word study progress."""


class WordStudyNetworkSourceABC(
    ABC,
):
    """ABC for Word study presentation network source."""

    @abstractmethod
    def fetch_presentation(self) -> schemas.WordStudyCaseSchema:
        """Fetch Word study presentation case."""


# Word study params sources
# -------------------------

ParamsNotifyT = Literal['initial_params_updated']


class WordParamsNotifyABC(ABC):
    """ABC for Word study params notifications."""

    @abstractmethod
    def initial_params_updated(self, params: schemas.WordParamsSchema) -> None:
        """Set Initial Word study params."""


class WordParamsLocaleSourceABC(
    ObserverManagerGenABC[WordParamsNotifyABC],
    ABC,
):
    """ABC for Word study params Locale source."""

    @abstractmethod
    def set_initial_params(self, params: schemas.WordParamsSchema) -> None:
        """Save initial Word study params."""


class WordParamsNetworkSourceABC(
    ABC,
):
    """ABC for Word study params source."""

    @abstractmethod
    def fetch_initial_params(self) -> schemas.WordParamsSchema:
        """Fetch Word study initial params."""
