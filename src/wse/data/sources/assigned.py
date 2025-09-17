"""Assigned exercise data source."""

from dataclasses import replace
from typing import Literal

from wse.data.entities.assigned import AssignedExercise
from wse.data.sources.base.source import SourceGen
from wse.feature.shared.schemas.exercise import Assigned

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
