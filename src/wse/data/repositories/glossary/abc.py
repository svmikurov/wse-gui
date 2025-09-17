"""Abstract base classes for Glossary repositories."""

from abc import ABC, abstractmethod

from wse.feature.api.glossary.schema import TermSchema


class TermsRepoABC(ABC):
    """ABC for term repository."""

    @abstractmethod
    def get_terms(self) -> list[TermSchema] | None:
        """Get terms."""
