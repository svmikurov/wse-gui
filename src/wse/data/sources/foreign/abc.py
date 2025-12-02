"""Abstract base classes for Foreign discipline sources."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Literal

from wse.feature.observer.generic import ObserverManagerGenABC

if TYPE_CHECKING:
    from wse.data.dto import foreign as dto
    from wse.data.schemas import foreign as schemas

# Word study source
# -----------------


class WordPresentationLocaleSourceABC(ABC):
    """Word study locale source."""

    @abstractmethod
    def set_case(self, case: schemas.PresentationCase) -> None:
        """Set Word study case."""

    @abstractmethod
    def get_case_uuid(self) -> str:
        """Get case UUID."""

    @abstractmethod
    def get_presentation_data(self) -> schemas.Presentation:
        """Get Presentation part of Word study."""


class WordStudyProgressNetworkSourceABC(ABC):
    """Word study progress Network Source."""

    @abstractmethod
    def increment_progress(self, case_uuid: str) -> None:
        """Increment Word study progress."""

    @abstractmethod
    def decrement_progress(self, case_uuid: str) -> None:
        """Decrement Word study progress."""


class WordPresentationNetworkSourceABC(
    ABC,
):
    """ABC for Word study presentation network source."""

    @abstractmethod
    def fetch_presentation(
        self,
        params: dto.InitialParameters,
    ) -> schemas.PresentationCase:
        """Fetch Word study presentation case."""


# Word study parameters sources
# -----------------------------

ParamsNotifyT = Literal['params_updated', 'initial_updated']


class WordParametersNotifyABC(ABC):
    """ABC for Word study parameters notifications."""

    @abstractmethod
    def params_updated(
        self,
        params: dto.PresentationParameters,
    ) -> None:
        """Update Word study parameters."""

    @abstractmethod
    def initial_updated(
        self,
        params: dto.InitialParameters,
    ) -> None:
        """Update Word study initial parameters."""


class WordParametersLocaleSourceABC(
    ObserverManagerGenABC[WordParametersNotifyABC],
    ABC,
):
    """ABC for Word study parameters Locale source."""

    @abstractmethod
    def update(
        self,
        data: dto.PresentationParameters | dto.InitialParameters,
    ) -> None:
        """Update Word study parameters."""

    @abstractmethod
    def set_initial(self, data: dto.InitialParameters) -> None:
        """Set Word study initial parameters."""

    @abstractmethod
    def get_initial(self) -> dto.InitialParameters:
        """Get Word study initial parameters."""

    @abstractmethod
    def refresh_initial(self) -> None:
        """Refresh observers data with initial parameters."""


class WordParametersNetworkSourceABC(
    ABC,
):
    """ABC for Word study parameters source."""

    @abstractmethod
    def fetch(self) -> dto.PresentationParameters:
        """Fetch Word study parameters."""

    @abstractmethod
    def save(
        self,
        data: dto.InitialParameters,
    ) -> dto.PresentationParameters:
        """Save Word study initial parameters."""
