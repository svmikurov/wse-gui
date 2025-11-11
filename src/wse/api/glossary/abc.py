"""Abstract Base Classes for Glossary discipline API clients."""

from abc import ABC, abstractmethod

from wse.api.glossary import schemas


class TermApiABC(ABC):
    """ABC for Term API client."""

    @abstractmethod
    def fetch_terms(self) -> schemas.TermsData | None:
        """Fetch terms."""


class TermPresentationApiABC(ABC):
    """ABC for Term Presentation API client."""

    @abstractmethod
    def fetch_presentation(
        self,
        payload: schemas.TermPresentationParamsSchema,
    ) -> schemas.TermPresentationSchema | None:
        """Fetch presentation."""
