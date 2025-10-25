"""Abstract Base Classes for Glossary discipline API clients."""

from abc import ABC, abstractmethod

from wse.api.glossary.schemas import (
    TermPresentationParamsSchema,
    TermPresentationSchema,
    TermsData,
)


class TermApiABC(ABC):
    """ABC for Term API client."""

    @abstractmethod
    def fetch_terms(self) -> TermsData | None:
        """Fetch terms."""


class TermPresentationApiABC(ABC):
    """ABC for Term Presentation API client."""

    @abstractmethod
    def fetch_presentation(
        self,
        payload: TermPresentationParamsSchema,
    ) -> TermPresentationSchema | None:
        """Fetch presentation."""
