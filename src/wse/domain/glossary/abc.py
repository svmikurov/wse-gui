"""Abstract base classes for Glossary discipline sources."""

from abc import ABC, abstractmethod

from wse.data.sources.glossary.term import TermNetworkSourceListenerABC

from ..abc import SubscribeUseCaseABC


class SubscribeTermsUseCaseABC(
    SubscribeUseCaseABC[TermNetworkSourceListenerABC],
    ABC,
):
    """ABC for Use Case to subscribe listener Terms notifications."""

    @abstractmethod
    def add_listener(self, listener: TermNetworkSourceListenerABC) -> None:
        """Add a new listener to this data source."""

    @abstractmethod
    def remove_listener(self, listener: TermNetworkSourceListenerABC) -> None:
        """Remove a listener from this data source."""


class GetTermsUseCaseABC(ABC):
    """ABC for get Terms Use Case."""

    @abstractmethod
    def get_terms(self) -> None:
        """Get terms."""


class TermPresentationUseCaseABC(ABC):
    """ABC for Presentation Use Case."""

    @abstractmethod
    def get_presentation(self) -> None:
        """Get presentation."""
