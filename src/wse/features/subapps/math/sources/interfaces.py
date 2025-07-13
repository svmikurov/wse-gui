"""Defines Math data sources interfaces."""

from typing import Protocol, Type

from wse_exercises.base.enums import ExerciseEnum

from wse.features.sources.interfaces import ISelectionSource
from wse.features.subapps.math.sources.selection import ExerciseEntry


class IExerciseSelectionSource(
    ISelectionSource[ExerciseEnum],
    Protocol,
):
    """Protocol for Exercise selection data source."""

    @property
    def entry_dto_type(self) -> Type[ExerciseEntry]:
        """Get DTO type to wrap entry."""
