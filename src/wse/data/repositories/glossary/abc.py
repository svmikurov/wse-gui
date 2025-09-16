"""Abstract base classes for Glossary repositories."""

from abc import ABC, abstractmethod

from wse.data.entities import Term


class TermRepoABC(ABC):
    """ABC for term repository."""

    @abstractmethod
    def get_terms(self) -> list[Term] | None:
        """Get terms."""
