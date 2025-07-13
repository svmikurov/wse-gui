"""Defines Main Math page view."""

from dataclasses import dataclass
from typing import Type

import toga
from injector import inject
from typing_extensions import override
from wse_exercises.base.enums import ExerciseEnum

from wse.config.layout import StyleConfig, ThemeConfig
from wse.features.base import BaseView
from wse.features.shared.widgets.interfaces import IFlexColumnStub
from wse.features.subapps.nav_id import NavID
from wse.utils.contextmanager import EventDisabler
from wse.utils.i18n import label_, nav_

from ...sources.interfaces import IExerciseSelectionSource
from .interfaces import IIndexMathView


@inject
@dataclass
class IndexMathView(
    BaseView,
    IIndexMathView,
):
    """Main Math page view."""

    # Sources injection
    _exercise_source: IExerciseSelectionSource

    # Widgets injection
    _flex_stub: Type[IFlexColumnStub]

    @override
    def _setup(self) -> None:
        self._content.test_id = NavID.INDEX_MATH

    @override
    def _populate_content(self) -> None:
        self.content.add(
            self._label_title,
            self._exercise_selection,
            self._btn_start,
            self._flex_stub(),
            self._btn_back,
        )

    @override
    def _create_ui(self) -> None:
        self._label_title = toga.Label('')
        self._exercise_selection = toga.Selection(
            accessor='accessor',
            items=self._exercise_source,
            on_change=self._on_exercise_change,
        )
        self._btn_start = toga.Button(on_press=self._handle_start_pressed)
        self._btn_back = self._create_nav_btn(nav_id=NavID.BACK)

    @override
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        self._label_title.style.update(**config.label_title)
        self._btn_back.style.update(**config.btn_nav)
        self._btn_start.style.update(**config.btn_nav)
        self._exercise_selection.style.update(**config.selection)

    @override
    def localize_ui(self) -> None:
        """Localize the UI text."""
        self._label_title.text = label_('Main math page title')
        self._btn_start.text = nav_(NavID.SIMPLE_CALC)
        self._btn_back.text = nav_(NavID.BACK)

    # Button callback functions

    def _handle_start_pressed(self, _: toga.Button) -> None:
        """Handle the start exercise button pressed."""
        self._notify('start_button_pressed')

    # API for controller

    @override
    def update_exercise_selection(self, exercises: list[ExerciseEnum]) -> None:
        """Update the Exercise selection data source."""
        with EventDisabler(self._exercise_selection):
            self._exercise_selection.items.update(exercises)

    def _on_exercise_change(self, selection: toga.Selection) -> None:
        self._notify('exercise_changed', value=selection.value.entry)
