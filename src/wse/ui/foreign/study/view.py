"""Foreign words study View."""

from dataclasses import dataclass
from typing import override

import toga
from injector import inject

from wse.config.layout.style import StyleConfig
from wse.config.layout.theme import ThemeConfig
from wse.core.navigation import NavID
from wse.ui.base.navigate.mixin import NavigateViewMixin
from wse.ui.containers.presentation.presenter import LabelAccessorContainerABC
from wse.ui.containers.top_bar.abc import TopBarControllerABC

from . import StudyForeignViewABC, StudyForeignViewModelABC


@inject
@dataclass
class StudyForeignView(
    NavigateViewMixin,
    StudyForeignViewABC,
):
    """Foreign words study View."""

    _state: StudyForeignViewModelABC
    _top_bar: TopBarControllerABC
    _presenter: LabelAccessorContainerABC

    @override
    def __post_init__(self) -> None:
        """Configure the view."""
        self._top_bar.add_observer(self)
        self._state.add_observer(self._presenter)
        self._content.test_id = NavID.FOREIGN_STUDY
        super().__post_init__()

    @override
    def _create_ui(self) -> None:
        self._title = toga.Label(NavID.FOREIGN_STUDY)

    @override
    def _populate_content(self) -> None:
        self._content.add(
            self._top_bar.content,
            self._title,
            self._presenter.content,
        )

    @override
    def localize_ui(self) -> None:
        return

    @override
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        self._title.style.update(**config.label_title)

    def on_open(self) -> None:
        """Call methods on screen open."""
        self._state.on_open()

    # TODO: Add to base class the subject
    # if `on_close` method is not define?
    def on_close(self) -> None:
        """Call methods before close the screen."""
        self._top_bar.remove_observer(self)
        self._state.remove_observer(self._presenter)
