"""Word study params View."""

from dataclasses import dataclass
from typing import override

import toga
from injector import inject

from wse.config.layout.style import StyleConfig
from wse.config.layout.theme import ThemeConfig
from wse.core.navigation import NavID

# TODO: Rename 'wse.ui.base.iwidgets'
from wse.ui.base.iwidgets import NavigableButton
from wse.ui.base.navigate.mixin import NavigateViewMixin
from wse.ui.containers.top_bar.abc import TopBarControllerABC
from wse.utils.i18n import I18N

from . import WordStudyParamsViewABC, WordStudyParamsViewModelABC


@inject
@dataclass
class WordStudyParamsView(
    NavigateViewMixin,
    WordStudyParamsViewABC,
):
    """Word study params View."""

    _top_bar: TopBarControllerABC
    _state: WordStudyParamsViewModelABC

    def __post_init__(self) -> None:
        """Construct the View."""
        self._state.add_observer(self)
        self._top_bar.add_observer(self)
        super().__post_init__()

    @override
    def _create_ui(self) -> None:
        self._title = toga.Label(I18N.NAV(NavID.FOREIGN_PARAMS))
        self._btn_start = self._create_nav_btn(NavID.FOREIGN_STUDY)

    @override
    def _populate_content(self) -> None:
        self._content.add(
            self._top_bar.content,
            self._title,
            self._btn_start,
        )

    @override
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        self._title.style.update(**config.label_title)
        self._btn_start.style.update(**config.btn_nav)

    @override
    def localize_ui(self) -> None:
        """Localize widgets."""
        # self._btn_start.text = I18N.NAV(NavID.FOREIGN_STUDY)

    @override
    def on_close(self) -> None:
        """Call methods before close the screen."""
        self._state.add_observer(self)
        self._top_bar.add_observer(self)

    # TODO: Move `_handle_navigate` to mixin?
    def _handle_navigate(self, button: NavigableButton) -> None:
        """Handle navigation button press."""
        self._state.navigate(button.nav_id)
