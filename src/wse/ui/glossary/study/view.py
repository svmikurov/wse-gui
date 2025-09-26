"""Terms study View."""

from dataclasses import dataclass

import toga
from injector import inject
from typing_extensions import override

from wse.config.layout import StyleConfig, ThemeConfig
from wse.core.navigation import NavID
from wse.feature.audit import AuditMixin
from wse.ui.base.content.abc import ContentABC
from wse.ui.containers.top_bar.abc import TopBarControllerABC
from wse.utils.i18n import label_

from ...base.navigate.mixin import NavigateViewMixin
from ...containers.presentation import PresentationContainerABC
from . import TermsStudyViewABC, TermsStudyViewModelABC


@inject
@dataclass
class TermsStudyView(
    AuditMixin,
    NavigateViewMixin,
    TermsStudyViewABC,
):
    """Terms study View."""

    _state: TermsStudyViewModelABC

    _top_bar: TopBarControllerABC
    _presentation: PresentationContainerABC

    def __post_init__(self) -> None:
        """Construct the View."""
        super().__post_init__()
        self._top_bar.add_observer(self)
        self._state.add_observer(self._presentation)

    def _create_ui(self) -> None:
        self._title = toga.Label(label_(NavID.TERMS_STUDY))

    def _populate_content(self) -> None:
        self._content.add(
            self._top_bar.content,
            self._title,
            self._presentation.content,
        )

    def localize_ui(self) -> None:
        """Localize UI."""
        # Deprecated
        pass

    def on_open(self) -> None:
        """Call methods on screen open."""
        self._state.refresh_context()

    @override
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        self._title.style.update(**config.label_title)

    def on_close(self) -> None:
        """Call methods on screen close event."""
        self._top_bar.remove_observer(self)

    @property
    def content(self) -> ContentABC:
        """Get page content."""
        return self._content
