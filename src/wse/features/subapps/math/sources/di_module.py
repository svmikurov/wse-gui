"""Defines Math data sources module."""

from typing import no_type_check

from injector import Binder, Module

from ..sources.interfaces import IExerciseSelectionSource
from ..sources.selection import ExerciseSelectionSource


class MathSourcesModule(Module):
    """Simple Math calculation data sources module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(IExerciseSelectionSource, to=ExerciseSelectionSource)
