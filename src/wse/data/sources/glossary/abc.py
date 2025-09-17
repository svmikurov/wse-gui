"""Abstract base classes for Glossary discipline sources."""

from abc import ABC, abstractmethod

from wse.feature.api.glossary.schema import TermSchema


class TermNetworkSourceABC(ABC):
    """ABC for Term Network source."""

    @abstractmethod
    def get_terms(self) -> list[TermSchema] | None:
        """Get terms."""
