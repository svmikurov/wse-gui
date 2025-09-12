"""Data layer repository DI module."""

from typing import no_type_check

from injector import Binder, Module

from .abc import HomeRepoABC
from .calculation_exercise import CalculationExerciseRepo
from .calculation_task import CalculationTaskRepo
from .home import HomeRepo
from .http_related import (
    RelatedDataHttpResponseRepo,
    RelatedDataHttpResponseRepoABC,
)
from .protocol import CalculationRepoProto
from .user import UserRepo, UserRepoABC


class RepoModule(Module):
    """Data layer repository DI module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(CalculationRepoProto, to=CalculationTaskRepo)
        binder.bind(CalculationExerciseRepo)
        binder.bind(
            RelatedDataHttpResponseRepoABC, to=RelatedDataHttpResponseRepo
        )
        binder.bind(UserRepoABC, to=UserRepo)
        binder.bind(HomeRepoABC, to=HomeRepo)
