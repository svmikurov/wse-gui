"""Defines Main Math page view."""

from dataclasses import dataclass

import toga
from injector import inject
from typing_extensions import override
from wse_exercises.core import MathEnum

from wse.apps.nav_id import NavID
from wse.config.layout import StyleConfig, ThemeConfig
from wse.feature.base import View
from wse.feature.shared.containers.top_bar import TopBarViewMixin
from wse.feature.source_wraps import ExerciseSelectWrapperProto
from wse.ui.math.index.abc import MathModelObserver
from wse.ui.math.index.state import MathIndexViewModel
from wse.utils.contextmanager import EventDisabler
from wse.utils.i18n import _, label_


@inject
@dataclass
class MathIndexView(
    TopBarViewMixin,
    View,
    MathModelObserver,
):
    """Main Math page view."""

    _state: MathIndexViewModel
    _exercise_selections_wrapper: ExerciseSelectWrapperProto

    @override
    def __post_init__(self) -> None:
        """Construct the view."""
        super().__post_init__()
        self._state.add_observer(self)
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
            items=self._exercise_selections_wrapper,
            on_change=self._state.change_exercise,
        )
        self._btn_start = toga.Button(on_press=self._state.start_exercise)

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

    @override
    def navigate(self, nav_id: NavID) -> None:
        """Navigate."""
        self._state.navigate(nav_id)

    def on_open(self) -> None:
        """Call methods on page open."""
        self._state.update_context()

    # ViewModel observe

    @override
    def exercises_updated(self, values: list[MathEnum]) -> None:
        """Update exercises select data source."""
        with EventDisabler(self._exercise_select):
            self._exercise_select.items.update(values)

    @override
    def exercise_selected(self, value: MathEnum) -> None:
        """Set selected exercise to choices."""
        # The selection is stored as an enumeration of entity instances.
        entity = self._exercise_select.items.find(value)
        self._exercise_select.value = entity
