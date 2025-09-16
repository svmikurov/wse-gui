"""Assigned exercises UI view."""

from dataclasses import dataclass

import toga
from injector import inject
from typing_extensions import override

from wse.config.layout import StyleConfig, ThemeConfig
from wse.core.navigation.nav_id import NavID
from wse.feature.shared.containers.assigned.abc import AssignationsContainerABC
from wse.feature.shared.containers.top_bar.abc import TopBarControllerABC
from wse.feature.shared.schemas.exercise import ExerciseInfo
from wse.utils.i18n import label_

from .abc import (
    AssignationsViewABC,
    AssignationsViewModelABC,
)


@inject
@dataclass
class AssignationsView(AssignationsViewABC):
    """Assigned exercises UI view."""

    _state: AssignationsViewModelABC

    # UI
    _top_bar: TopBarControllerABC
    _exercises: AssignationsContainerABC

    def __post_init__(self) -> None:
        """Construct the view."""
        super().__post_init__()
        self._exercises.add_observer(self)
        self._state.add_observer(self)
        self._top_bar.add_observer(self)

    @override
    def _populate_content(self) -> None:
        self.content.add(
            self._top_bar.content,
            self._label_title,
            self._exercises.content,
        )

    @override
    def _create_ui(self) -> None:
        self._label_title = toga.Label('')

    @override
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        self._label_title.style.update(**config.label_title)

    @override
    def localize_ui(self) -> None:
        """Localize the UI text."""
        self._label_title.text = label_('Assigned exercises title')

    def on_open(self) -> None:
        """Call methods on screen open."""
        self._state.refresh_context()

    def navigate(self, nav_id: NavID) -> None:
        """Navigate."""
        self._state.navigate(nav_id)

    # IU state observe

    @override
    def exercises_updated(self, exercises: list[ExerciseInfo]) -> None:
        """Update view on update exercises event."""
        self._exercises.update_exercises(exercises)

    # Assigned exercises container observe

    def exercise_selected(self, assignation_id: str) -> None:
        """Notify that exercise selected."""
        self._state.start_exercise(assignation_id=assignation_id)

    def on_close(self) -> None:
        """Call methods before close the screen."""
        self._exercises.remove_observer(self)
        self._top_bar.remove_observer(self)
        self._state.remove_observer(self)
        self._state.on_close()
