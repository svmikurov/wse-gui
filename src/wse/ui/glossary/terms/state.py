"""Terms screen UI state."""

from dataclasses import dataclass, replace
from typing import TypedDict

from injector import inject
from typing_extensions import Unpack

from wse.core.interfaces import Navigable
from wse.data.entities.term import Term
from wse.data.repositories.glossary import TermsRepoABC
from wse.feature.base.audit import AuditMixin
from wse.ui.base.mixin import NavigateStateMixin
from wse.ui.glossary.terms import TermsViewModelABC


class _DataFieldType(TypedDict, total=False):
    """Types for UI data state fields."""

    terms: list[Term] | None


@dataclass(frozen=True)
class TermsUIState:
    """Terms UI state data."""

    terms: list[Term] | None = None


@inject
@dataclass
class TermsViewModel(
    AuditMixin,
    NavigateStateMixin,
    TermsViewModelABC,
):
    """Terms screen ViewModel."""

    _navigator: Navigable

    _terms_repo: TermsRepoABC

    def refresh_context(self) -> None:
        """Refresh screen context."""
        term_schemas = self._terms_repo.get_terms()
        if term_schemas is not None:
            terms = [Term(**term.to_dict()) for term in term_schemas]
            print('===========================================')
            print(f'{terms = }')
            print('===========================================')

    def _create_data(self) -> None:
        """Create UI state data."""
        self._data = TermsUIState()

    # TODO: Move to ABC Generic[...UIState] class.
    def _update_data(self, **data: Unpack[_DataFieldType]) -> None:
        """Update UI state data."""
        self._data = replace(self._data, **data)
