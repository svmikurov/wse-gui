"""Defines Math data sources module."""

from typing import no_type_check

from injector import Binder, Module

from ..sources import ExerciseSelectSourceProto
from ..sources.selection import ExerciseSelectSource


class MathSourcesModule(Module):
    """Simple Math calculation data sources module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(ExerciseSelectSourceProto, to=ExerciseSelectSource)
