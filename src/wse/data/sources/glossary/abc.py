"""Abstract base classes for Glossary discipline sources."""

from abc import ABC, abstractmethod

from wse.data.entities.term import Term


class TermNetworkSourceABC(ABC):
    """ABC for Term Network source."""

    @abstractmethod
    def get_terms(self) -> list[Term] | None:
        """Get terms."""
