"""DI module for Simple Math calculation page module."""

from typing import no_type_check

from injector import Binder, Module

from wse.apps.math.sources import ExerciseSelectSourceProto
from wse.apps.math.sources.selection import ExerciseSelectSource

from .controller import CalculationController
from .model import CalculationModel
from .protocols import (
    CalculationControllerProto,
    CalculationModelProto,
)


class CalculationModule(Module):
    """Simple Math calculation page module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        # MVC model
        binder.bind(CalculationModelProto, to=CalculationModel)
        binder.bind(CalculationControllerProto, to=CalculationController)

        # Sources
        binder.bind(ExerciseSelectSourceProto, to=ExerciseSelectSource)
