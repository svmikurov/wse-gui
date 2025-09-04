"""Defines Assigned exercises page controller."""

from dataclasses import dataclass

from injector import inject
from typing_extensions import override

from wse.apps.nav_id import NavID
from wse.core.interfaces import NavigatorProto
from wse.feature.base.mvc import PageController

from .abc import (
    AssignationsViewObserver,
)
from .protocols import (
    AssignationsModelProto,
    AssignationsViewProto,
)


class _ViewObserve(
    AssignationsViewObserver,
):
    """Mixin providing observe of assigned view event."""

    _model: AssignationsModelProto
    _navigator: NavigatorProto

    @override
    def exercise_selected(self, assignation_id: str) -> None:
        """Handle the view event on exercise select."""
        exercise_api = self._model.fetch_exercise(assignation_id)
        if exercise_api:
            self._navigator.navigate(nav_id=NavID.EXERCISE, value=exercise_api)


@inject
@dataclass
class AssignationsController(
    _ViewObserve,
    PageController[AssignationsModelProto, AssignationsViewProto, None],
):
    """Assigned exercises page controller."""

    _model: AssignationsModelProto
    _view: AssignationsViewProto

    def on_open(self, value: None = None) -> None:
        """Call methods when page opens."""
        self._model.fetch_exercises()
