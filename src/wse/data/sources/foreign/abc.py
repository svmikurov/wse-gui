"""Abstract base classes for Foreign discipline sources."""

from abc import ABC, abstractmethod
from typing import Literal

from wse.feature.observer.generic import ObserverManagerGenABC

from .schemas import (
    WordParamsSchema,
    WordStudyPresentationSchema,
    WordStudySettingsSchema,
)

# Word study settings
# -------------------


class WordStudySettingsLocaleSourceABC(ABC):
    """Word study Locale settings source."""

    @abstractmethod
    def get_settings(self) -> WordStudySettingsSchema:
        """Get word study settings."""


# Word study source
# -----------------


class WordStudyPresentationNetworkSourceABC(
    ABC,
):
    """ABC for Word study presentation network source."""

    @abstractmethod
    def fetch_presentation(self) -> WordStudyPresentationSchema:
        """Fetch Word study presentation case."""


# Word study params sources
# -------------------------

ParamsNotifyT = Literal['initial_params_updated']


class WordParamsNotifyABC(ABC):
    """ABC for Word study params notifications."""

    @abstractmethod
    def initial_params_updated(self, params: WordParamsSchema) -> None:
        """Set Initial Word study params."""


class WordParamsLocaleSourceABC(
    ObserverManagerGenABC[WordParamsNotifyABC],
    ABC,
):
    """ABC for Word study params Locale source."""

    @abstractmethod
    def set_initial_params(self, params: WordParamsSchema) -> None:
        """Save initial Word study params."""


class WordParamsNetworkSourceABC(
    ABC,
):
    """ABC for Word study params source."""

    @abstractmethod
    def fetch_initial_params(self) -> WordParamsSchema:
        """Fetch Word study initial params."""
