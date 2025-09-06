"""Defines Assigned exercises page view."""

from dataclasses import dataclass
from typing import Literal

import toga
from injector import inject
from typing_extensions import override

from wse.apps.main.pages.assignations import (
    AssignationsModelProto,
    AssignationsViewFeatureProto,
)
from wse.apps.main.pages.assignations.abc import (
    AssignationsModelObserver,
    AssignationsViewFeature,
    BaseAssignationsView,
)
from wse.config.layout import StyleConfig, ThemeConfig
from wse.feature.base.mixins import AddObserverGen
from wse.feature.shared.containers.assigned import (
    AssignationsContainerProto,
)
from wse.feature.shared.containers.top_bar import TopBarViewMixin
from wse.feature.shared.schemas.exercise import ExerciseInfo
from wse.utils.i18n import label_

_NotifyType = Literal['exercise_selected']


class _Feature(
    AssignationsViewFeature,
    AddObserverGen[_NotifyType],
):
    """Assigned page view feature."""

    _exercises: AssignationsContainerProto

    @override
    def update_exercises(self, exercises: list[ExerciseInfo]) -> None:
        """Update exercises to display."""
        self._exercises.update_exercises(exercises)

    @override
    def exercise_selected(self, assignation_id: str) -> None:
        """Notify that exercise selected."""
        self._notify('exercise_selected', assignation_id=assignation_id)


class _ModelObserve(
    AssignationsModelObserver,
    AssignationsViewFeatureProto,
):
    """Mixin providing observe of assigned model event."""

    @override
    def exercises_updated(self, exercises: list[ExerciseInfo]) -> None:
        """Update view on update exercises event."""
        self.update_exercises(exercises)


@inject
@dataclass
class AssignationsView(
    _Feature,
    _ModelObserve,
    TopBarViewMixin,
    BaseAssignationsView[AssignationsModelProto],
):
    """Assigned exercises page view."""

    _exercises: AssignationsContainerProto

    def _setup(self) -> None:
        super()._setup()
        self._exercises.add_observer(self)

    @override
    def _populate_content(self) -> None:
        self.content.add(
            self._top_bar.content,  # Provided by `TopBarPageViewMixin`
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
