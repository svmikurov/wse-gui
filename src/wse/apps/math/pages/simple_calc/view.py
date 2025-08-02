"""Defines Simple math calculation page view."""

from dataclasses import dataclass
from typing import Type

import toga
from injector import inject
from typing_extensions import override

from wse.apps.nav_id import NavID
from wse.config.layout import StyleConfig, ThemeConfig
from wse.features.base import BaseView
from wse.features.shared.containers.interfaces import (
    INumPadController,
    ITextTaskContainer,
)
from wse.features.shared.containers.top_bar import TopBarPageViewMixin
from wse.features.shared.widgets.interfaces import (
    IDivider,
    IFlexColumnStub,
)
from wse.utils.i18n import _, label_


@inject
@dataclass
class SimpleCalcView(
    TopBarPageViewMixin,
    BaseView,
):
    """Simple math calculation page view."""

    # Containers injection
    _task_panel: ITextTaskContainer
    _numpad: INumPadController

    # Widgets injections
    _divider: Type[IDivider]
    _flex_stub: Type[IFlexColumnStub]

    @override
    def _setup(self) -> None:
        super()._setup()
        self._content.test_id = NavID.SIMPLE_CALC
        self._numpad.add_observer(self)

    # Layout methods

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
        self._btn_submit = toga.Button('', on_press=self._confirm_answer)
        self._btn_next = toga.Button('', on_press=self._next_task)

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

    # Callback button functions

    def _confirm_answer(self, _: toga.Button) -> None:
        """Handle the confirm answer event."""
        self._notify('answer_confirmed')

    def _next_task(self, _: toga.Button) -> None:
        """Handle the start next task event."""
        self._notify('task_started')
        self._set_submit_btn()
        self._enable_buttons()

    # Notifications from NumPad

    def numpad_input_updated(self, value: str) -> None:
        """Update user input."""
        self._notify('numpad_input_updated', value=value)

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
        self._numpad.clear_input()

    def display_correct_answer(self, value: str) -> None:
        """Display the correct answer."""
        self._task_panel.display_correct_answer(value)
        self._set_next_btn()
        self._disable_buttons()

    # Widget management

    def reset_layout(self) -> None:
        """Reset to initial layout."""
        self._set_submit_btn()
        self._enable_buttons()

    def _set_next_btn(self) -> None:
        self.content.replace(self._btn_submit, self._btn_next)

    def _set_submit_btn(self) -> None:
        try:
            self.content.replace(self._btn_next, self._btn_submit)
        except ValueError:
            # The button is already sets
            pass

    def _disable_buttons(self) -> None:
        self._numpad.disable_buttons()

    def _enable_buttons(self) -> None:
        self._numpad.enable_buttons()
