"""Assigned exercise data source."""

from dataclasses import replace
from typing import Literal

from wse.data.dto.assigned import AssignedExercise
from wse.data.schemas.exercise import Assigned
from wse.data.sources.base.source import SourceGen

_SourceNotifyT = Literal['']


class AssignedSourceObserverABC:
    """ABC for Assigned exercise data source observer.

    Not implemented yet.
    """


class AssignedExerciseSource(
    SourceGen[AssignedSourceObserverABC, _SourceNotifyT],
):
    """Assigned exercise data source."""

    def __init__(self) -> None:
        """Construct the source."""
        super().__init__()
        # This is the single source of troth, not injected.
        self._exercise = AssignedExercise()

    def set_exercise(self, exercise: Assigned) -> None:
        """Set assigned exercise."""
        self._exercise = replace(self._exercise, **exercise.to_dict())

    @property
    def data(self) -> AssignedExercise:
        """Get Assigned exercise source data."""
        return self._exercise
