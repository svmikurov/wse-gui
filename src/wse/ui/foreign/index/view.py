"""Index Foreign discipline view."""

from dataclasses import dataclass
from typing import override

import toga
from injector import inject
from toga.style import Pack

from wse.config.layout import StyleConfig, ThemeConfig
from wse.core.navigation import NavID
from wse.feature.audit import AuditMixin
from wse.ui.base.iwidgets import NavigableButton
from wse.ui.base.navigate.mixin import NavigateViewMixin
from wse.ui.containers.top_bar.abc import TopBarControllerABC
from wse.utils.i18n import label_

from .abc import IndexForeignViewABC, IndexForeignViewModelABC


@inject
@dataclass
class IndexForeignView(
    AuditMixin,
    NavigateViewMixin,
    IndexForeignViewABC,
):
    """Index Foreign discipline view."""

    _state: IndexForeignViewModelABC

    _top_bar: TopBarControllerABC

    @override
    def __post_init__(self) -> None:
        """Construct the view."""
        super().__post_init__()
        self._top_bar.add_observer(self)

    @override
    def _create_ui(self) -> None:
        self._title = toga.Label(
            label_(NavID.FOREIGN),
            # TODO: May be refactor style injection?
            style=Pack(**self._style.label_title, **self._theme.label_title),  # type: ignore[arg-type]
        )

    @override
    def _populate_content(self) -> None:
        self._content.add(
            self._top_bar.content,
            self._title,
        )

    # Deprecated `localize_ui` method?
    # TODO: Remove `localize_ui` abstract method?
    @override
    def localize_ui(self) -> None:
        """Localize the UI text."""
        pass

    # Deprecated `update_style` method?
    # TODO: Remove `update_style` abstract method?
    @override
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        pass

    @override
    def on_close(self) -> None:
        """Call methods before close the screen."""
        self._top_bar.remove_observer(self)

    # Callback methods

    # TODO: Move `_handle_navigate` to mixin?
    @override
    def _handle_navigate(self, button: NavigableButton) -> None:
        """Handle navigation button press."""
        self._state.navigate(button.nav_id)
