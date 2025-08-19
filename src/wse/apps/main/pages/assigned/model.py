"""Defines Assigned exercises page model."""

from dataclasses import dataclass

from injector import inject

from wse.apps.nav_id import NavID
from wse.features.base import BaseModel

from ...http.iapi import IAssignedExercisesApi
from .iabc import AssignedModelABC


@inject
@dataclass
class AssignedModel(
    BaseModel,
    AssignedModelABC,
):
    """Assigned exercises page model."""

    _api_service: IAssignedExercisesApi

    def on_open(self) -> None:
        """Call methods when page opens."""
        exercises = self._api_service.request_all_exercises()
        if exercises is not None:
            self._notify('exercises_updated', exercises=exercises)

    def goto_exercise(self, assignation_id: str) -> None:
        """Go to selected exercise."""
        exercise_meta_dto = self._api_service.request_selected(assignation_id)
        self._notify('navigate', nav_id=NavID.EXERCISE, meta=exercise_meta_dto)
