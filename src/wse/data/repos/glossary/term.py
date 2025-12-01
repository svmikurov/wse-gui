"""Term repository."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from injector import inject

from wse.data.sources.glossary import TermNetworkSourceABC

from . import TermsRepoABC

if TYPE_CHECKING:
    from wse.api.glossary import schemas


@inject
@dataclass
class TermsRepo(TermsRepoABC):
    """Term repository."""

    _term_source: TermNetworkSourceABC

    def get_terms(self) -> list[schemas.Term] | None:
        """Get terms."""
        return self._term_source.get_terms()
