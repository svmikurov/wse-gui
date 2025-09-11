"""Data layer repository DI module."""

from typing import no_type_check

from injector import Binder, Module

from .calculation_exercise import CalculationExerciseRepo
from .calculation_task import CalculationTaskRepo
from .protocol import CalculationRepoProto


class RepoModule(Module):
    """Data layer repository DI module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(CalculationRepoProto, to=CalculationTaskRepo)
        binder.bind(CalculationExerciseRepo)
