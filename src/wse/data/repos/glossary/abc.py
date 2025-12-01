"""Abstract base classes for Glossary repositories."""

from abc import ABC, abstractmethod

from wse.api.glossary.schemas import Term


class TermsRepoABC(ABC):
    """ABC for term repository."""

    @abstractmethod
    def get_terms(self) -> list[Term] | None:
        """Get terms."""


class TermPresentationRepoABC(ABC):
    """ABC for Term Presentation repo."""

    @abstractmethod
    def get_presentation(self) -> None:
        """Get presentation."""
