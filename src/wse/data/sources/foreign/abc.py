"""Abstract base classes for Foreign discipline sources."""

from abc import ABC, abstractmethod
from typing import Literal

from wse.api.foreign import requests, schemas
from wse.feature.observer.generic import ObserverManagerGenABC

# Word study source
# -----------------


class WordStudyLocaleSourceABC(ABC):
    """Word study locale source."""

    @abstractmethod
    def set_case(self, case: schemas.PresentationCase) -> None:
        """Set Word study case."""

    @abstractmethod
    def get_case_uuid(self) -> str:
        """Get case UUID."""

    @abstractmethod
    def get_presentation_data(self) -> schemas.PresentationSchema:
        """Get Presentation part of Word study."""


class WordStudyProgressNetworkSourceABC(ABC):
    """Word study progress Network Source."""

    @abstractmethod
    def increment_progress(self, case_uuid: str) -> None:
        """Increment Word study progress."""

    @abstractmethod
    def decrement_progress(self, case_uuid: str) -> None:
        """Decrement Word study progress."""


class WordStudyNetworkSourceABC(
    ABC,
):
    """ABC for Word study presentation network source."""

    @abstractmethod
    def fetch_presentation(
        self,
        params: requests.InitialParametersDTO,
    ) -> schemas.PresentationCase:
        """Fetch Word study presentation case."""


# Word study params sources
# -------------------------

ParamsNotifyT = Literal['initial_params_updated']


class WordParamsNotifyABC(ABC):
    """ABC for Word study params notifications."""

    @abstractmethod
    def initial_params_updated(
        self,
        params: requests.PresentationParamsDTO,
    ) -> None:
        """Set Initial Word study params."""


class WordParamsLocaleSourceABC(
    ObserverManagerGenABC[WordParamsNotifyABC],
    ABC,
):
    """ABC for Word study params Locale source."""

    @abstractmethod
    def set_initial_params(self, data: requests.SelectedParameters) -> None:
        """Save initial Word study params."""

    @abstractmethod
    def update_initial_params(self, data: object) -> None:
        """Save initial Word study params."""

    @abstractmethod
    def get_params(self) -> requests.InitialParametersDTO:
        """Get Word study Presentation params."""


class WordParamsNetworkSourceABC(
    ABC,
):
    """ABC for Word study params source."""

    @abstractmethod
    def fetch_params(self) -> requests.PresentationParamsDTO:
        """Fetch Word study params."""

    # TODO: Fix static types.
    @abstractmethod
    def save_initial_params(self, data: requests.InitialParametersDTO) -> bool:
        """Save Word study initial params."""
