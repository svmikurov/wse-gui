"""Terms screen UI state."""

from dataclasses import dataclass

from injector import inject
from toga.sources import Source
from typing_extensions import override

from wse.core.interfaces import Navigable
from wse.data.entities.term import Term
from wse.data.sources.base.source import EntrySourceGen
from wse.domain.glossary import (
    GetTermsUseCaseABC,
    SubscribeTermsUseCaseABC,
)
from wse.feature.base.audit import AuditMixin
from wse.ui.base.mixin import NavigateStateMixin
from wse.ui.glossary.terms import TermsViewModelABC


class TermsTableSource(  # type: ignore[misc] ## `Source` is incompatible with definition
    EntrySourceGen[Term],
    # The `toga.Table` widget programmatically subscribes to a source
    # if it `data` attribute is of the `toga.source.Source` subtype.
    Source,
):
    """Terms table data state source.

    DI provides this source as singleton.
    """


@inject
@dataclass
class TermsViewModel(
    AuditMixin,
    NavigateStateMixin,
    TermsViewModelABC,
):
    """Terms screen ViewModel."""

    _navigator: Navigable

    _subscribe_terms_case: SubscribeTermsUseCaseABC
    _get_terms_case: GetTermsUseCaseABC
    _table_state: TermsTableSource

    def __post_init__(self) -> None:
        """Construct the ViewModel."""
        self._subscribe_terms_case.add_listener(self)

    @override
    def refresh_context(self) -> None:
        """Refresh screen context."""
        self._get_terms_case.get_terms()

    @override
    def updated(self, terms: list[Term]) -> None:
        """Handle the data source updated event."""
        self._table_state.clear()
        for term in terms:
            self._table_state.add(term)

    @override
    def on_close(self) -> None:
        """Call methods before close the screen."""
        self._subscribe_terms_case.remove_listener(self)
