"""Term repository."""

from dataclasses import dataclass

from injector import inject

from ...entities import Term
from ...sources.glossary import TermNetworkSourceABC
from . import TermRepoABC


@inject
@dataclass
class TermRepo(TermRepoABC):
    """ABC for term repository."""

    _term_source: TermNetworkSourceABC

    def get_terms(self) -> list[Term] | None:
        """Get terms."""
        return self._term_source.get_terms()
