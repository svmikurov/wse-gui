"""Defines Math data sources module."""

from typing import no_type_check

from injector import Binder, Module

from ..source_wraps import ExerciseSelectWrapperProto
from ..source_wraps.selection import ExerciseSelectSourceWrap


class MathSourceWrapsModule(Module):
    """Simple Math calculation data sources module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(ExerciseSelectWrapperProto, to=ExerciseSelectSourceWrap)
