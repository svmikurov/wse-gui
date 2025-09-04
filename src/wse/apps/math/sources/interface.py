"""Defines Math data sources interfaces."""

from typing import Protocol, Type

from wse_exercises.base.enums import ExerciseEnum

from wse.apps.math.sources.selection import ExerciseEntry
from wse.feature.sources import SelectSourceProto


class ExerciseSelectSourceProto(
    SelectSourceProto[ExerciseEnum],
    Protocol,
):
    """Protocol for Exercise selection data source."""

    @property
    def entry_type(self) -> Type[ExerciseEntry]:
        """Get type to wrap entry."""
