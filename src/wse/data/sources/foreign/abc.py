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
    def get_settings(self) -> schemas.PresentationSettings:
        """Get Word study settings."""


# Word study source
# -----------------


class WordStudyLocaleSourceABC(ABC):
    """Word study locale source."""

    @abstractmethod
    def set_case(self, case: schemas.PresentationCase) -> None:
        """Set Word study case."""

    @abstractmethod
    def get_case_uuid(self) -> uuid.UUID:
        """Get case UUID."""

    @abstractmethod
    def get_presentation_data(self) -> schemas.PresentationSchema:
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
    def fetch_presentation(
        self,
        params: schemas.PresentationParams,
    ) -> schemas.PresentationCase:
        """Fetch Word study presentation case."""


# Word study params sources
# -------------------------

ParamsNotifyT = Literal['initial_params_updated']


class WordParamsNotifyABC(ABC):
    """ABC for Word study params notifications."""

    @abstractmethod
    def initial_params_updated(self, params: schemas.ParamsChoices) -> None:
        """Set Initial Word study params."""


class WordParamsLocaleSourceABC(
    ObserverManagerGenABC[WordParamsNotifyABC],
    ABC,
):
    """ABC for Word study params Locale source."""

    @abstractmethod
    def set_initial_params(self, params: schemas.ParamsChoices) -> None:
        """Save initial Word study params."""

    @abstractmethod
    def get_params(self) -> schemas.PresentationParams:
        """Get Word study Presentation params."""


class WordParamsNetworkSourceABC(
    ABC,
):
    """ABC for Word study params source."""

    @abstractmethod
    def fetch_initial_params(self) -> schemas.ParamsChoices:
        """Fetch Word study initial params."""
