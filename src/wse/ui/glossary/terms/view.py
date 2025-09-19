"""Terms View."""

from dataclasses import dataclass

import toga
from injector import inject
from typing_extensions import override

from wse.config import StyleConfig, ThemeConfig
from wse.core.navigation import NavID
from wse.feature.base.audit import AuditMixin
from wse.feature.interfaces.iwidgets import NavigableButton
from wse.ui.containers.top_bar.abc import TopBarControllerABC
from wse.utils.i18n import _

from ...base.mixin import NavigateViewMixin
from . import TermsViewABC, TermsViewModelABC
from .state import TermsTableSource


@inject
@dataclass
class TermsView(
    AuditMixin,
    NavigateViewMixin,
    TermsViewABC,
):
    """Terms View."""

    _state: TermsViewModelABC

    _top_bar: TopBarControllerABC
    _table_state: TermsTableSource

    @override
    def __post_init__(self) -> None:
        """Construct the view."""
        super().__post_init__()
        self._top_bar.add_observer(self)

    @override
    def _create_ui(self) -> None:
        self._title = toga.Label('')
        self._table = toga.Table(
            # After creating a table, cannot localize the header text.
            headings=[_('Term'), _('Definition')],
            accessors=['name', 'definition'],
            data=self._table_state,
        )

    @override
    def _populate_content(self) -> None:
        self._content.add(
            self._top_bar.content,
            self._title,
            self._table,
        )

    @override
    def localize_ui(self) -> None:
        """Localize the UI text."""
        self._title.text = NavID.TERMS

    @override
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        self._title.style.update(**config.label_title)
        # TODO: Add style for table

    def on_open(self) -> None:
        """Call methods on page open."""
        self._state.refresh_context()

    @override
    def on_close(self) -> None:
        """Call methods before close the screen."""
        self._top_bar.remove_observer(self)

    @override
    def _handle_navigate(self, button: NavigableButton) -> None:
        self._state.navigate(button.nav_id)
