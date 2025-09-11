"""Exercise view with integer I/O UI."""

from dataclasses import dataclass
from typing import Literal, Type

import toga
from injector import inject
from typing_extensions import override

from wse.apps.nav_id import NavID
from wse.config.layout import StyleConfig, ThemeConfig
from wse.feature.base.mvc import ViewGen
from wse.feature.base.mvc_exercise import ExerciseModelObserverABC
from wse.feature.interfaces.iobserver import Observable
from wse.feature.shared.containers import (
    NumpadControllerProto,
    NumpadObserverABC,
    TextTaskContainerProto,
)
from wse.feature.shared.containers.top_bar import TopBarViewMixin
from wse.feature.shared.widgets import (
    DividerProto,
    FlexColumnStubProto,
)
from wse.utils.i18n import _, label_

_NotifyType = Literal[
    'task_started',
    'answer_entered',
    'answer_submitted',
]


@inject
@dataclass
class IntegerView(
    TopBarViewMixin,
    ExerciseModelObserverABC,
    NumpadObserverABC,
    ViewGen[_NotifyType],
):
    """Exercise view with integer I/O UI."""

    _subject: Observable
    _task_panel: TextTaskContainerProto
    _numpad: NumpadControllerProto

    # Widgets injections
    _divider: Type[DividerProto]
    _flex_stub: Type[FlexColumnStubProto]

    @override
    def __post_init__(self) -> None:
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
        self._btn_submit = toga.Button('', on_press=self._submit_answer)
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

    def numpad_entered(self, value: str) -> None:
        """Update user input."""
        self._notify('answer_entered', value=value)

    def balance_updated(self, value: str) -> None:
        """Handle balance update event notification."""
        self._top_bar.update_balance(value)

    # Callback

    def _submit_answer(self, _: toga.Button) -> None:
        """Handle the confirm answer event."""
        if self._task_panel.answer != '':
            self._notify('answer_submitted')

    def _next_task(self, _: toga.Button) -> None:
        """Handle the start next task event."""
        self._reset_layout()
        self._notify('task_started')

    # Model observer

    @override
    def task_updated(self, value: str) -> None:
        """Handle the model event on task update."""
        self._reset_layout()
        self._task_panel.display_question(value)

    @override
    def answer_updated(self, value: str) -> None:
        """Handle the model event on answer update."""
        self._task_panel.display_answer(value)

    @override
    def answer_incorrect(self, value: str) -> None:
        """Handle the model event on success answer checking."""
        self._task_panel.display_correct_answer(value)
        self._set_next_btn()
        self._numpad.disable_buttons()

    # Utility

    def _reset_layout(self) -> None:
        """Reset to initial layout."""
        self._set_submit_btn()
        self._task_panel.clear_question()
        self._task_panel.clear_answer()
        self._numpad.clear_input()
        self._numpad.enable_buttons()

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
