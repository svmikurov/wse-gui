"""Calculation exercise view."""

from dataclasses import dataclass
from typing import Literal, Type

import toga
from injector import inject
from typing_extensions import override

from wse.apps.nav_id import NavID
from wse.config.layout import StyleConfig, ThemeConfig
from wse.feature.base import View
from wse.feature.base.mixins import AddObserverGen
from wse.feature.shared.containers import (
    BaseNumpadObserver,
    NumpadControllerProto,
    TextTaskContainerProto,
)
from wse.feature.shared.containers.top_bar import TopBarViewMixin
from wse.feature.shared.widgets import (
    DividerProto,
    FlexColumnStubProto,
)
from wse.utils.i18n import _, label_

from .abc import CalculationViewModelObserverABC
from .protocol import CalculationViewModelProto

_NotifyType = Literal['navigate']


@inject
@dataclass
class CalculationView(
    TopBarViewMixin,
    BaseNumpadObserver,
    CalculationViewModelObserverABC,
    View,
    AddObserverGen[_NotifyType],
):
    """Calculation exercise view."""

    _state: CalculationViewModelProto
    _task_panel: TextTaskContainerProto
    _numpad: NumpadControllerProto

    # Widgets injections
    _divider: Type[DividerProto]
    _flex_stub: Type[FlexColumnStubProto]

    def __post_init__(self) -> None:
        """Construct the view."""
        super().__post_init__()
        self._content.test_id = NavID.SIMPLE_CALC
        self._numpad.add_observer(self)
        self._state.add_observer(self)

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
        self._btn_submit = toga.Button('', on_press=self._state.submit_answer)
        self._btn_next = toga.Button('', on_press=self._state.update_task)

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

    # Feature

    @override
    def navigate(self, nav_id: NavID) -> None:
        """Navigate."""
        self._state.navigate(nav_id)

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

    @override
    def state_reset(self) -> None:
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
        self._state.update_answer(answer=value)

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
