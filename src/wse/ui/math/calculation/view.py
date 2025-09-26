"""Calculation exercise View."""

from dataclasses import dataclass

import toga
from injector import inject
from typing_extensions import override

from wse.config.layout import StyleConfig, ThemeConfig
from wse.core.navigation.nav_id import NavID
from wse.feature.audit import AuditMixin
from wse.ui.containers.numpad.protocols import NumPadControllerABC
from wse.ui.containers.task_panel import (
    TextTaskContainerABC,
)
from wse.ui.containers.top_bar.abc import TopBarControllerABC
from wse.ui.widgets import DividerType, FlexColumnStubType
from wse.utils.i18n import _, label_

from ...base.navigate.mixin import NavigateViewMixin
from .abc import CalculationViewABC, CalculationViewModelABC


@inject
@dataclass
class CalculationView(
    AuditMixin,
    NavigateViewMixin,
    CalculationViewABC,
):
    """Calculation exercise view."""

    _state: CalculationViewModelABC

    # Widget injection
    _top_bar: TopBarControllerABC
    _task_panel: TextTaskContainerABC
    _numpad: NumPadControllerABC
    _divider: DividerType
    _flex_stub: FlexColumnStubType

    def __post_init__(self) -> None:
        """Construct the view."""
        super().__post_init__()
        self._content.test_id = NavID.CALCULATION
        self._top_bar.add_observer(self)
        self._numpad.add_observer(self)  # type: ignore[arg-type]
        self._state.add_observer(self)

    @override
    def _populate_content(self) -> None:
        self.content.add(
            self._top_bar.content,
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
        self._btn_submit = toga.Button('', on_press=self._state.submit_answer)  # type: ignore[arg-type]
        self._btn_next = toga.Button('', on_press=self._state.update_task)  # type: ignore[arg-type]

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

    def on_open(self) -> None:
        """Call methods on page open."""
        self._state.start_task()

    # State holder observe

    @override
    def question_updated(self, question: str) -> None:
        """Handle the model event on task update."""
        self._task_panel.display_question(question)

    @override
    def answer_updated(self, answer: str) -> None:
        """Handle the model event on task update."""
        self._task_panel.display_answer(answer)

    @override
    def answer_incorrect(self) -> None:
        """Handle the model event on incorrect answer."""
        self._set_next_btn()
        self._numpad.disable_buttons()

    @override
    def solution_updated(self, solution: str) -> None:
        """Display correct solution."""
        self._task_panel.display_correct_answer(solution)

    def balance_updated(self, balance: str) -> None:
        """Handle the balance updated state event."""
        self._top_bar.update_balance(balance)

    @override
    def task_reset(self) -> None:
        """Handle the model event on task update."""
        self._task_panel.clear_question()
        self._task_panel.clear_answer()
        self._numpad.clear_input()
        self._set_submit_btn()
        self._numpad.enable_buttons()

    # Numpad observe

    @override
    def numpad_entered(self, value: str) -> None:
        """Update user input."""
        self._state.update_answer(value=value)

    # Utility methods

    def _set_next_btn(self) -> None:
        try:
            self.content.replace(self._btn_submit, self._btn_next)
        except ValueError:
            # The button is already sets
            pass

    def _set_submit_btn(self) -> None:
        try:
            self.content.replace(self._btn_next, self._btn_submit)
        except ValueError:
            # The button is already sets
            pass

    # On screen close

    @override
    def on_close(self) -> None:
        """Call methods before close the screen."""
        self._top_bar.remove_observer(self)
        self._numpad.remove_observer(self)  # type: ignore[arg-type]
        self._state.remove_observer(self)
        self._state.on_close()
