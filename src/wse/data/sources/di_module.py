"""Data sources DI module."""

from typing import no_type_check

from injector import Binder, Module, SingletonScope

from . import (
    AssignedExerciseSource,
    CalculationExerciseSource,
    TaskSource,
)
from .glossary import TermNetworkSourceABC
from .glossary.term import TermNetworkSource
from .user import UserSource


class SourceModule(Module):
    """Data sources DI module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        # Core
        binder.bind(UserSource, scope=SingletonScope)

        # Task
        binder.bind(TaskSource, scope=SingletonScope)

        # Calculation
        binder.bind(CalculationExerciseSource, scope=SingletonScope)

        # Assigned
        binder.bind(AssignedExerciseSource, scope=SingletonScope)

        # Glossary
        binder.bind(TermNetworkSourceABC, to=TermNetworkSource)
