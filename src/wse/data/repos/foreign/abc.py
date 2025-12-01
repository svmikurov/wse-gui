"""Abstract base classes for Foreign discipline repositories."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from wse.data.dto import foreign as dto
    from wse.data.schemas import foreign as schemas
    from wse.data.sources.foreign import WordParametersNotifyABC

# Study repo
# ----------


class WordProgressRepoABC(ABC):
    """ABC for Word study progress repository."""

    @abstractmethod
    def increment(self) -> None:
        """Increment Word study progress."""

    @abstractmethod
    def decrement(self) -> None:
        """Decrement Word study progress."""


class WordPresentationRepoABC(ABC):
    """ABC Word study presentation repository."""

    @abstractmethod
    def get_word(self) -> schemas.Presentation:
        """Get word to study."""


# Study params repo
# -----------------


class RefreshWordParametersRepositoryABC(ABC):
    """ABC for refresh Word study parameters repository."""

    @abstractmethod
    def fetch(self) -> None:
        """Set available params, default for Word study params.

        These params come from external source (API) and define what
        params user can choose from.
        """


class WordParametersSubscriberABC(ABC):
    """Word study params Source mapper."""

    @abstractmethod
    def subscribe(self, observer: WordParametersNotifyABC) -> None:
        """Subscribe observer to Word params source notifications."""

    @abstractmethod
    def unsubscribe(self, observer: WordParametersNotifyABC) -> None:
        """Unsubscribe observer to Word params source notifications."""


class WordParametersRepoABC(
    RefreshWordParametersRepositoryABC,
    ABC,
):
    """ABC for Word study repository."""

    @abstractmethod
    def fetch(self) -> None:
        """Fetch Word study parameters."""

    @abstractmethod
    def get(self) -> dto.InitialParameters:
        """Get Word study initial parameters."""

    @abstractmethod
    def set(self, data: dto.InitialParameters) -> None:
        """Set Word study initial parameters."""

    @abstractmethod
    def save(self, data: dto.InitialParameters) -> None:
        """Save Word study parameters."""

    @abstractmethod
    def refresh(self) -> None:
        """Refresh Word study parameters."""


# TODO: Delete below


class SetWordParametersRepoABC(ABC):
    """ABC for repository to set Word study params."""

    @abstractmethod
    def set_params(self, params: schemas.PresentationParameters) -> None:
        """Set available params, default values for Word study params.

        These params come from external source (API) and define what
        params user can choose from.
        """

    @abstractmethod
    def set_selected_params(
        self,
        params: schemas.SelectedParameters,
    ) -> None:
        """Set user's current selection for Word study params.

        These params represent actual choices made by user in the UI
        and should be persisted for session continuity.
        """
