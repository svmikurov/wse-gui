"""Abstract base classes for Foreign discipline repositories."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from wse.data.sources.foreign import schemas

if TYPE_CHECKING:
    from wse.data.sources.foreign import WordParamsNotifyABC

# Study repo
# ----------


class WordStudyProgressRepoABC(ABC):
    """Word study progress repo."""

    @abstractmethod
    def increment(self) -> None:
        """Increment Word study progress."""

    @abstractmethod
    def decrement(self) -> None:
        """Decrement Word study progress."""


class WordStudyRepoABC(ABC):
    """ABC for repository to get words to study."""

    @abstractmethod
    def get_word(self) -> schemas.WordPresentationSchema:
        """Get word to study."""


# Study params repo
# -----------------


class RefreshWordParamsRepoABC(ABC):
    """ABC for repository to refresh Word study params."""

    @abstractmethod
    def refresh_initial_params(self) -> None:
        """Set available params, default for Word study params.

        These params come from external source (API) and define what
        params user can choose from.
        """


class WordParamsMapperABC(ABC):
    """Word study params Source mapper."""

    @abstractmethod
    def subscribe(self, observer: WordParamsNotifyABC) -> None:
        """Subscribe observer to Word params source notifications."""

    @abstractmethod
    def unsubscribe(self, observer: WordParamsNotifyABC) -> None:
        """Unsubscribe observer to Word params source notifications."""


class WordParamsRepoABC(
    RefreshWordParamsRepoABC,
):
    """ABC for Word study repository."""


class WordStudySettingsRepoABC(ABC):
    """ABC for Word study settings repository."""

    @abstractmethod
    def get_settings(self) -> schemas.WordStudySettingsSchema:
        """Get word study settings."""


# TODO: Delete below


class SetWordParamsRepoABC(ABC):
    """ABC for repository to set Word study params."""

    @abstractmethod
    def set_initial_params(self, params: schemas.WordParamsSchema) -> None:
        """Set available params, default values for Word study params.

        These params come from external source (API) and define what
        params user can choose from.
        """

    @abstractmethod
    def set_selected_params(self, params: schemas.WordSelectedSchema) -> None:
        """Set user's current selection for Word study params.

        These params represent actual choices made by user in the UI
        and should be persisted for session continuity.
        """
