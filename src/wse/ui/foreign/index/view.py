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
from wse.ui.widgets.buttons import NavButton
from wse.utils.i18n import I18N, label_

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
        self._btn_study = self._create_nav_btn(NavID.FOREIGN_STUDY)

    @override
    def _populate_content(self) -> None:
        self._content.add(
            self._top_bar.content,
            self._title,
            self._btn_study,
        )

    # Deprecated `localize_ui` method?
    # TODO: Remove `localize_ui` abstract method?
    @override
    def localize_ui(self) -> None:
        """Localize the UI text."""
        self._btn_study.text = I18N.NAV(NavID.FOREIGN_STUDY)

    # Deprecated `update_style` method?
    # TODO: Remove `update_style` abstract method?
    @override
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        self._btn_study.style.update(**config.btn_nav)

    @override
    def on_close(self) -> None:
        """Call methods before close the screen."""
        self._top_bar.remove_observer(self)

    # Callback methods

    def _create_nav_btn(self, nav_id: NavID) -> NavigableButton:
        """Create navigation button."""
        return NavButton(nav_id=nav_id, on_press=self._handle_navigate)

    # TODO: Move `_handle_navigate` to mixin?
    def _handle_navigate(self, button: NavigableButton) -> None:
        """Handle navigation button press."""
        self._state.navigate(button.nav_id)
