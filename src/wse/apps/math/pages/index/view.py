"""Defines Main Math page view."""

from dataclasses import dataclass
from typing import Literal

import toga
from injector import inject
from typing_extensions import override
from wse_exercises.base.enums import ExerciseEnum

from wse.apps.math.pages.index.abc import MathModelObserver
from wse.apps.math.sources import ExerciseSelectSourceProto
from wse.apps.nav_id import NavID
from wse.config.layout import StyleConfig, ThemeConfig
from wse.feature.base import View
from wse.feature.base.mixins import AddObserverGen
from wse.feature.shared.containers.top_bar import TopBarViewMixin
from wse.utils.contextmanager import EventDisabler
from wse.utils.i18n import _, label_

_NotifyType = Literal[
    'start_button_pressed',
    'exercise_changed',
]


class _Utility:
    """Mixin providing utility methods for Index Math page view."""

    _exercise_select: toga.Selection

    def _update_exercise_select(self, exercises: list[ExerciseEnum]) -> None:
        """Update the Exercise selection widget with exercises."""
        with EventDisabler(self._exercise_select):
            self._exercise_select.items.update(exercises)

    def _set_selected_exercise(self, value: ExerciseEnum) -> None:
        """Set selected exercise to choices."""
        item = self._exercise_select.items.find(value)
        self._exercise_select.value = item


class _ModelObserver(
    _Utility,
    MathModelObserver,
):
    """Mixin providing observe on Index Math page model."""

    @override
    def exercises_updated(self, values: list[ExerciseEnum]) -> None:
        """Update exercises select data source."""
        self._update_exercise_select(values)

    @override
    def exercise_selected(self, value: ExerciseEnum) -> None:
        """Set selected exercise to choices."""
        self._set_selected_exercise(value)


class _Callback(
    AddObserverGen[_NotifyType],
):
    """Mixin provides Index Math page model callback function."""

    # Button callback function

    def _handle_start_pressed(self, _: toga.Button) -> None:
        """Handle the start exercise button pressed."""
        self._notify('start_button_pressed')

    # Selection callback function

    def _on_exercise_change(self, selection: toga.Selection) -> None:
        """Handle the exercise changed selection event."""
        self._notify('exercise_changed', value=selection.value.entry)


@inject
@dataclass
class MathView(
    TopBarViewMixin,
    View,
    _ModelObserver,
    _Callback,
):
    """Main Math page view."""

    _exercise_source: ExerciseSelectSourceProto

    @override
    def __post_init__(self) -> None:
        """Construct the view."""
        super().__post_init__()
        self._content.test_id = NavID.INDEX_MATH

    @override
    def _populate_content(self) -> None:
        self.content.add(
            self._top_bar.content,
            self._label_title,
            self._exercise_select,
            self._btn_start,
        )

    @override
    def _create_ui(self) -> None:
        self._label_title = toga.Label('')
        self._exercise_select = toga.Selection(
            accessor='accessor',
            items=self._exercise_source,
            on_change=self._on_exercise_change,
        )
        self._btn_start = toga.Button(on_press=self._handle_start_pressed)

    @override
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        self._label_title.style.update(**config.label_title)
        self._btn_start.style.update(**config.btn_nav)
        self._exercise_select.style.update(**config.selection)

    @override
    def localize_ui(self) -> None:
        """Localize the UI text."""
        self._label_title.text = label_('Main math page title')
        self._btn_start.text = _('Start exercise')
