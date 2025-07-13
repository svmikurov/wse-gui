"""Defines Simple math calculation page view."""

from dataclasses import dataclass
from typing import Type

import toga
from injector import inject
from typing_extensions import override

from wse.config.layout import StyleConfig, ThemeConfig
from wse.features.base import BaseView
from wse.features.shared.containers.interfaces import (
    INumPadController,
    ITextTaskContainer,
)
from wse.features.shared.widgets.interfaces import (
    IDivider,
    IFlexColumnStub,
)
from wse.features.subapps.nav_id import NavID
from wse.utils.i18n import _, label_, nav_

from .interfaces import ISimpleCalcView


@inject
@dataclass
class SimpleCalcView(BaseView, ISimpleCalcView):
    """Simple math calculation page view."""

    # Containers injection
    _task_panel: ITextTaskContainer
    _numpad: INumPadController

    # Widgets injections
    _divider: Type[IDivider]
    _flex_stub: Type[IFlexColumnStub]

    @override
    def _setup(self) -> None:
        self._content.test_id = NavID.SIMPLE_CALC
        self._numpad.add_observer(self)

    # Layout methods

    @override
    def _populate_content(self) -> None:
        self.content.add(
            self._label_title,
            self._divider(),
            self._task_panel.content,
            self._flex_stub(),
            self._divider(),
            self._numpad.content,
            self._divider(),
            self._btn_submit,
            self._btn_back,
        )

    @override
    def _create_ui(self) -> None:
        self._label_title = toga.Label('')
        self._btn_back = self._create_nav_btn(nav_id=NavID.BACK)
        self._btn_submit = toga.Button('', on_press=self._confirm_answer)

    @override
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        self._label_title.style.update(**config.label_title)
        self._btn_back.style.update(**config.btn_nav)
        self._btn_submit.style.update(**config.button)

    @override
    def localize_ui(self) -> None:
        """Localize the UI text."""
        self._label_title.text = label_('Simple calculation title')
        self._btn_back.text = nav_(NavID.BACK)
        self._btn_submit.text = _('Send answer')

    # Callback button functions

    def _confirm_answer(self, _: toga.Button) -> None:
        """Handle the confirm answer event."""
        self._notify('answer_confirmed')

    # Notifications from NumPad

    @override
    def numpad_input_updated(self, value: str) -> None:
        """Update user input."""
        self._notify('numpad_input_updated', value=value)

    # API for controller

    @override
    def display_question(self, value: str) -> None:
        """Display the question."""
        self._task_panel.display_question(value)

    @override
    def clear_question(self) -> None:
        """Clear the question text."""
        self._task_panel.clear_question()

    @override
    def display_answer(self, value: str) -> None:
        """Display the user answer."""
        self._task_panel.display_answer(value)

    @override
    def clear_answer(self) -> None:
        """Clear the question text."""
        self._task_panel.clear_answer()
        self._numpad.clear_input()
