"""Assigned exercise data source."""

from abc import ABC
from typing import Literal

from wse.data.entities.assigned import AssignedExercise
from wse.data.sources.base.source import DataSourceGen

_SourceNotifyT = Literal['']


class AssignedSourceObserverABC(ABC):
    """ABC for Assigned exercise data source observer."""


class AssignedSource(
    DataSourceGen[AssignedSourceObserverABC, _SourceNotifyT],
):
    """Assigned exercise data source."""

    def __init__(self) -> None:
        """Construct the source."""
        super().__init__()
        # This is the single source of troth, not injected.
        self._exercise = AssignedExercise()

    @property
    def data(self) -> AssignedExercise:
        """Get Assigned exercise source data."""
        return self._exercise
