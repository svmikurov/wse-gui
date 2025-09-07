"""Calculation exercise view."""

from dataclasses import dataclass
from typing import Type

import toga
from injector import inject
from typing_extensions import override

from wse.apps.nav_id import NavID
from wse.config.layout import StyleConfig, ThemeConfig
from wse.feature.base import View
from wse.feature.shared.containers import (
    NumpadControllerProto,
    TextTaskContainerProto,
)
from wse.feature.shared.containers.top_bar import TopBarViewMixin
from wse.feature.shared.widgets import (
    DividerProto,
    FlexColumnStubProto,
)
from wse.utils.i18n import _, label_

from .protocol import CalculationModelViewProto


@inject
@dataclass
class CalculationView(
    TopBarViewMixin,
    View,
):
    """Calculation exercise view."""

    _mv: CalculationModelViewProto
    _task_panel: TextTaskContainerProto
    _numpad: NumpadControllerProto

    # Widgets injections
    _divider: Type[DividerProto]
    _flex_stub: Type[FlexColumnStubProto]

    def __post_init__(self) -> None:
        """Construct the view."""
        super().__post_init__()
        self._numpad.add_observer(self)
        self._content.test_id = NavID.SIMPLE_CALC

    @override
    def _populate_content(self) -> None:
        self.content.add(
            self._top_bar.content,  # Provided by `TopBarPageViewMixin`
            self._label_title,
            self._divider(),
            self._task_panel.content,
            self._flex_stub(),
            self._divider(),
            self._numpad.content,
            self._divider(),
            self._btn_submit,
        )

    @override
    def _create_ui(self) -> None:
        self._label_title = toga.Label('')
        self._btn_submit = toga.Button('', on_press=self._mv.submit_answer)
        self._btn_next = toga.Button('', on_press=self._mv.get_task)

    @override
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        self._label_title.style.update(**config.label_title)
        self._btn_submit.style.update(**config.button)
        self._btn_next.style.update(**config.button)

    @override
    def localize_ui(self) -> None:
        """Localize the UI text."""
        self._label_title.text = label_('Simple calculation title')
        self._btn_submit.text = _('Send answer')
        self._btn_next.text = _('Next task')
