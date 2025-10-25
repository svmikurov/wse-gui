"""Term repository."""

from dataclasses import dataclass

from injector import inject

from wse.feature.api.glossary.schemas import TermSchema

from ...sources.glossary import TermNetworkSourceABC
from . import TermsRepoABC


@inject
@dataclass
class TermsRepo(TermsRepoABC):
    """ABC for terms repository."""

    _term_source: TermNetworkSourceABC

    def get_terms(self) -> list[TermSchema] | None:
        """Get terms."""
        return self._term_source.get_terms()
