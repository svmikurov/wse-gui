"""Term sources."""

from dataclasses import dataclass

from injector import inject

from wse.data.entities import Term
from wse.feature.api.glossary.abc import TermApiABC
from wse.feature.api.glossary.schema import TermsData

from . import TermNetworkSourceABC


@inject
@dataclass
class TermNetworkSource(TermNetworkSourceABC):
    """Term Network Source."""

    # TODO: Add source state storage of Terms response,
    #       such as next/previous pagination, ...

    _api_term: TermApiABC

    def get_terms(self) -> list[Term] | None:
        """Get terms."""
        terms = self._api_term.fetch_terms()
        if isinstance(terms, TermsData):
            return terms.results
        return None
