"""Defines Assigned exercises page model."""

from dataclasses import dataclass

from injector import inject

from wse.features.base import BaseModel

from ...http.dto import AssignedExercisesDTO
from ...http.iapi import IAssignedExercisesApi
from .iabc import AssignedModelABC


@inject
@dataclass
class AssignedModel(
    BaseModel,
    AssignedModelABC,
):
    """Assigned exercises page model."""

    # Injected API client for exercises data
    _api_assigned: IAssignedExercisesApi

    def __post_init__(self) -> None:
        """Construct the model."""
        super().__post_init__()
        self.exercises: list[AssignedExercisesDTO] | None = None

    def on_open(self) -> None:
        """Call methods when page opens."""
        self._request_all_exercises()
        if self.exercises is not None:
            self._exercise_updated(self.exercises)

    def _request_all_exercises(self) -> None:
        """Request all assigned exercises for user."""
        self.exercises = self._api_assigned.request_all_exercises()

    # Controller notifications

    def _exercise_updated(self, exercises: list[AssignedExercisesDTO]) -> None:
        self._notify('exercises_updated', exercises=exercises)

    # Controller API

    def goto_exercise(self, exercise_id: str) -> None:
        """Go to selected exercise."""
