"""Data layer repository DI module."""

from typing import no_type_check

from injector import Binder, Module

from .abc import AssignedTaskRepoABC, CalculationTaskRepoABC
from .assigned_task import AssignedTaskRepo
from .calculation_exercises import CalculationExerciseRepo
from .calculation_task import CalculationTaskRepo
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
        binder.bind(CalculationTaskRepoABC, to=CalculationTaskRepo)
        binder.bind(CalculationExerciseRepo)
        binder.bind(UserRepoABC, to=UserRepo)
        binder.bind(AssignedTaskRepoABC, to=AssignedTaskRepo)
        binder.bind(InitialDataRepoABC, to=InitialDataRepo)

        binder.bind(
            RelatedDataHttpResponseRepoABC,
            to=RelatedDataHttpResponseRepo,
        )
