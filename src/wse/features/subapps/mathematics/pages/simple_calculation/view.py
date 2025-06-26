"""Defines Simple math calculation page view."""

from dataclasses import dataclass
from typing import Callable

import toga
from injector import inject

from wse.config.layout import StyleConfig, ThemeConfig
from wse.features.base import BaseView
from wse.features.interfaces import IObserver
from wse.features.shared.components.interfaces import INumPadController
from wse.features.shared.containers.interfaces import ITextTaskPanel
from wse.features.shared.widgets.interfaces import IDivider, IFlexColumnStub
from wse.features.subapps.nav_id import NavID
from wse.utils.i18n import label_, nav_


@inject
@dataclass
class SimpleCalcView(BaseView):
    """Simple math calculation page view."""

    _task_panel: ITextTaskPanel
    _numpad: INumPadController

    # Widgets
    _divider: Callable[[], IDivider]
    _flex_stub: Callable[[], IFlexColumnStub]

    def _setup(self) -> None:
        self._content.test_id = NavID.SIMPLE_CALC

    # Layout methods

    def _populate_content(self) -> None:
        self.content.add(
            self._label_title,
            self._divider(),
            self._task_panel.content,
            self._flex_stub(),
            self._divider(),
            self._numpad.content,
            self._divider(),
            self._btn_back,
        )

    def _create_ui(self) -> None:
        self._label_title = toga.Label('')
        self._btn_back = self._create_nav_btn(nav_id=NavID.BACK)

    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        self._label_title.style.update(**config.label_title)
        self._btn_back.style.update(**config.btn_nav)

    def localize_ui(self) -> None:
        """Localize the UI text."""
        self._label_title.text = label_('Simple calculation title')
        self._btn_back.text = nav_(NavID.BACK)

    # Observer methods

    def subscribe_to_numpad(self, observer: IObserver) -> None:
        """Subscribe observers to NumPad events."""
        self._numpad.add_observer(observer)

    # API for controller

    def display_question(self, value: str) -> None:
        """Display the question."""
        self._task_panel.display_question(value)

    def clear_question(self) -> None:
        """Clear the question text."""
        self._task_panel.clear_question()

    def display_answer(self, value: str) -> None:
        """Display the user answer."""
        self._task_panel.display_answer(value)

    def clear_answer(self) -> None:
        """Clear the question text."""
        self._task_panel.clear_answer()
