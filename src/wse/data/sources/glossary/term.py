"""Term sources."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Literal, TypedDict

from injector import inject

from wse.feature.api.glossary.abc import TermApiABC

from ...entities.term import Term, Terms
from ..base.source import SourceGen
from . import TermNetworkSourceABC

_NotifyT = Literal['updated']


class _SourceDateTypes(TypedDict, total=False):
    """Types for Terms data source fields."""

    count: int | None
    next_url: str | None
    previous_url: str | None
    terms: list[Term] | None


class TermNetworkSourceListenerABC(ABC):
    """ABC for Terms data source Observer."""

    @abstractmethod
    def updated(self, terms: list[Term]) -> None:
        """Handle the data source updated event."""


@inject
@dataclass
class TermNetworkSource(
    SourceGen[TermNetworkSourceListenerABC, _NotifyT],
    TermNetworkSourceABC,
):
    """Term Network Source."""

    _api_term: TermApiABC

    def __post_init__(self) -> None:
        """Construct the source."""
        self._terms = Terms()

    def get_terms(self) -> None:
        """Get terms."""
        self._fetch_terms()

    def _fetch_terms(self) -> None:
        """Fetch terms data."""
        if data := self._api_term.fetch_terms():
            if results := data.results:
                self._terms = Terms(
                    count=data.count,
                    next_url=data.next,
                    previous_url=data.previous,
                    terms=[Term(**term.to_dict()) for term in results],
                )

                self.notify('updated', terms=self._terms.terms)
        return None
