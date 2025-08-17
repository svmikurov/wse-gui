"""Defines Assigned exercises page view."""

from dataclasses import dataclass

import toga
from injector import inject
from typing_extensions import override

from wse.apps.main.http.dto import AssignedExerciseDTO
from wse.apps.main.pages.assigned.iabc import AssignedViewABC
from wse.config.layout import StyleConfig, ThemeConfig
from wse.features.base import BaseView
from wse.features.shared.containers.iabc.iassigned import IAssignedContainer
from wse.features.shared.containers.top_bar import TopBarPageViewMixin
from wse.utils.i18n import label_


@inject
@dataclass
class AssignedView(
    TopBarPageViewMixin,
    BaseView,
    AssignedViewABC,
):
    """Assigned exercises page view."""

    _exercises: IAssignedContainer

    def _setup(self) -> None:
        super()._setup()
        self._exercises.add_observer(self)

    @override
    def _create_ui(self) -> None:
        self._label_title = toga.Label('')

    @override
    def _populate_content(self) -> None:
        self.content.add(
            self._top_bar.content,  # Provided by `TopBarPageViewMixin`
            self._label_title,
            self._exercises.content,
        )

    # API

    @override
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        self._label_title.style.update(**config.label_title)

    @override
    def localize_ui(self) -> None:
        """Localize the UI text."""
        self._label_title.text = label_('Assigned exercises title')

    @override
    def update_exercises(self, exercises: list[AssignedExerciseDTO]) -> None:
        """Update exercises to display."""
        self._exercises.update_exercises(exercises)

    # Notification from Assigned exercises container

    def exersice_selected(self, value: str) -> None:
        """Notify that exercise selected."""
        self._notify('exercise_selected', value=value)
