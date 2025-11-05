"""Data sources DI module."""

from typing import no_type_check

from injector import Binder, Module, SingletonScope

from . import (
    AssignedExerciseSource,
    CalculationExerciseSource,
    TaskSource,
)
from .foreign import (
    WordParamsLocaleSourceABC,
    WordParamsNetworkSourceABC,
    WordStudyPresentationNetworkSourceABC,
    WordStudyProgressNetworkSourceABC,
    WordStudySettingsLocaleSourceABC,
)
from .foreign.params import (
    WordParamsData,
    WordParamsLocaleSource,
    WordParamsNetworkSource,
)
from .foreign.progress import WordStudyProgressNetworkSource
from .foreign.study import (
    WordStudyPresentationNetworkSource,
    WordStudySettingsData,
    WordStudySettingsLocaleSource,
)
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

        # Foreign: Word study
        binder.bind(
            WordStudyPresentationNetworkSourceABC,
            to=WordStudyPresentationNetworkSource,
            scope=SingletonScope,
        )
        binder.bind(
            WordStudySettingsLocaleSourceABC,
            to=WordStudySettingsLocaleSource,
            scope=SingletonScope,
        )
        binder.bind(
            WordStudySettingsData,
            scope=SingletonScope,
        )

        # Foreign: Word study params
        binder.bind(
            WordParamsData,
            scope=SingletonScope,
        )
        binder.bind(
            WordParamsLocaleSourceABC,
            to=WordParamsLocaleSource,
            scope=SingletonScope,
        )
        binder.bind(
            WordParamsNetworkSourceABC,
            to=WordParamsNetworkSource,
        )
        binder.bind(
            WordStudyProgressNetworkSourceABC,
            to=WordStudyProgressNetworkSource,
        )
