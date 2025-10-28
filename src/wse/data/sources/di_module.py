"""Data sources DI module."""

from typing import no_type_check

from injector import Binder, Module, SingletonScope

from . import (
    AssignedExerciseSource,
    CalculationExerciseSource,
    TaskSource,
)
from .foreign import params
from .foreign.abc import WordStudyPresentationNetworkSourceABC
from .foreign.study import WordStudyPresentationNetworkSource
from .glossary import TermNetworkSourceABC, TermPresentationNetworkSourceABC
from .glossary.study import TermPresentationNetworkSource
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
        binder.bind(
            TermNetworkSourceABC,
            to=TermNetworkSource,
            scope=SingletonScope,
        )
        binder.bind(
            TermPresentationNetworkSourceABC,
            to=TermPresentationNetworkSource,
            scope=SingletonScope,
        )

        # Foreign
        binder.bind(
            WordStudyPresentationNetworkSourceABC,
            to=WordStudyPresentationNetworkSource,
            scope=SingletonScope,
        )
        # Foreign: Word study params
        binder.bind(
            params.WordParamsData,
            scope=SingletonScope,
        )
        binder.bind(
            params.WordParamsLocaleSourceABC,
            to=params.WordParamsLocaleSource,
            scope=SingletonScope,
        )
        binder.bind(
            params.WordParamsNetworkSourceABC,
            to=params.WordParamsNetworkSource,
        )
