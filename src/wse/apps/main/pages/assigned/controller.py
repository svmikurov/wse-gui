"""Defines Assigned exercises page controller."""

from dataclasses import dataclass

from injector import inject
from typing_extensions import override

from wse.features.base.mvc import BasePageController

from ...http.dto import AssignedExercisesDTO
from .iabc import AssignedControllerABC, IAssignedModel, IAssignedView


@inject
@dataclass
class AssignedController(
    BasePageController,
    AssignedControllerABC,
):
    """Assigned exercises page controller."""

    # Injected page elements
    _model: IAssignedModel
    _view: IAssignedView

    def _setup(self) -> None:
        super()._setup()
        self._model.add_observer(self)

    @override
    def on_open(self, **kwargs: object) -> None:
        """Call methods when page opens."""
        self._model.on_open()

    # Notification from model

    @override
    def exercises_updated(self, exercises: list[AssignedExercisesDTO]) -> None:
        """Update view on update exercises event."""
        self._view.update_exercises(exercises)

    # Notification from view

    @override
    def exercise_selected(self, value: str) -> None:
        """Handle exercise selected event."""
        self._model.goto_exercise(value)
