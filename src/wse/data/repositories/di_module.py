"""Data layer repository DI module."""

from typing import no_type_check

from injector import Binder, Module

from . import (
    CalculationRepositoryProto,
)
from .calculation_task import CalculationTaskRepository


class RepositoryModule(Module):
    """Data layer repository DI module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(CalculationRepositoryProto, to=CalculationTaskRepository)
