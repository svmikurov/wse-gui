"""Index Glossary discipline screen UI."""

from dataclasses import dataclass

import toga
from injector import inject
from typing_extensions import override

from wse.config import StyleConfig, ThemeConfig
from wse.core.navigation import NavID
from wse.feature.base.audit import AuditMixin
from wse.feature.interfaces.iwidgets import NavigableButton
from wse.feature.shared.containers.top_bar.abc import TopBarControllerABC
from wse.utils.i18n import label_, nav_

from ...base.mixin import NavigateViewMixin
from . import IndexGlossaryViewABC, IndexGlossaryViewModelABC


@inject
@dataclass
class IndexGlossaryView(
    AuditMixin,
    NavigateViewMixin,
    IndexGlossaryViewABC,
):
    """Index Glossary screen View."""

    _state: IndexGlossaryViewModelABC

    _top_bar: TopBarControllerABC

    @override
    def __post_init__(self) -> None:
        """Construct the View."""
        super().__post_init__()
        self._top_bar.add_observer(self)

    @override
    def _create_ui(self) -> None:
        self._title = toga.Label('')
        self._btn_terms = self._create_nav_btn(NavID.TERMS)
        self._btn_study = self._create_nav_btn(NavID.TERMS_STUDY)

    @override
    def _populate_content(self) -> None:
        self._content.add(
            self._top_bar.content,
            self._title,
            self._btn_terms,
            self._btn_study,
        )

    @override
    def localize_ui(self) -> None:
        """Localize the UI text."""
        self._title.text = label_(NavID.GLOSSARY)
        self._btn_terms.text = nav_(NavID.TERMS)
        self._btn_study.text = nav_(NavID.TERMS_STUDY)

    @override
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        self._title.style.update(**config.label_title)
        self._btn_terms.style.update(**config.btn_nav)
        self._btn_study.style.update(**config.btn_nav)

    def on_open(self) -> None:
        """Call methods before close the screen."""
        self._state.refresh_content()

    @override
    def on_close(self) -> None:
        """Call methods before close the screen."""
        self._top_bar.remove_observer(self)

    # Callback

    def _handle_navigate(self, button: NavigableButton) -> None:
        """Handle navigation button press."""
        self._state.navigate(button.nav_id)
