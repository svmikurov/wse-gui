"""Data layer repository DI module."""

from typing import no_type_check

from injector import Binder, Module

from .abc import AssignedTaskRepoABC, CalculationTaskRepoABC
from .assigned_task import AssignedTaskRepo
from .calculation_exercises import CalculationExerciseRepo
from .calculation_task import CalculationTaskRepo
from .foreign import (
    GetWordStudyRepoABC,
    WordParamsMapperABC,
    WordParamsRepoABC,
    WordStudyProgressRepoABC,
    WordStudySettingsRepoABC,
)
from .foreign.params import WordParamsMapper, WordParamsRepo
from .foreign.progress import WordStudyProgressRepo
from .foreign.study import GetWordStudyRepo, WordStudySettingsRepo
from .glossary import TermPresentationRepoABC, TermsRepoABC
from .glossary.study import TermPresentationRepo
from .glossary.term import TermsRepo
from .http_related import (
    RelatedDataHttpResponseRepo,
    RelatedDataHttpResponseRepoABC,
)
from .initial import InitialDataRepo, InitialDataRepoABC
from .user import UserRepo, UserRepoABC


class RepoModule(Module):
    """Data layer repository DI module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        # Core
        binder.bind(InitialDataRepoABC, to=InitialDataRepo)
        binder.bind(
            RelatedDataHttpResponseRepoABC,
            to=RelatedDataHttpResponseRepo,
        )

        # User
        binder.bind(UserRepoABC, to=UserRepo)

        # Calculation
        binder.bind(CalculationTaskRepoABC, to=CalculationTaskRepo)
        # TODO: Add ABC to bind `CalculationExerciseRepo`
        binder.bind(CalculationExerciseRepo)

        # Assigned
        binder.bind(AssignedTaskRepoABC, to=AssignedTaskRepo)

        # Glossary
        binder.bind(TermsRepoABC, to=TermsRepo)
        binder.bind(TermPresentationRepoABC, to=TermPresentationRepo)

        # Foreign
        binder.bind(GetWordStudyRepoABC, to=GetWordStudyRepo)
        binder.bind(WordParamsRepoABC, to=WordParamsRepo)
        binder.bind(WordParamsMapperABC, to=WordParamsMapper)
        binder.bind(WordStudySettingsRepoABC, to=WordStudySettingsRepo)
        binder.bind(WordStudyProgressRepoABC, to=WordStudyProgressRepo)
