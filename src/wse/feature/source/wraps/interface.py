"""Defines Math data sources interfaces."""

from abc import ABC, abstractmethod
from typing import Type

from wse_exercises.base.enums import ExerciseEnum

from wse.feature.source import SelectSourceABC

from .selection import ExerciseEntry


class ExerciseSelectWrapperABC(
    SelectSourceABC[ExerciseEnum],
    ABC,
):
    """Protocol for Exercise selection data source wrap."""

    @property
    @abstractmethod
    def entry_type(self) -> Type[ExerciseEntry]:
        """Get type to wrap entry."""
