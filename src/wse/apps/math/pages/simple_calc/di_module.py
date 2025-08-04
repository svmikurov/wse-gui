"""Defines Simple Math calculation page module."""

from typing import no_type_check

from injector import Binder, Module

from ...sources.interfaces import IExerciseSelectionSource
from ...sources.selection import ExerciseSelectionSource
from .controller import CalcController
from .interfaces import (
    ICalcController,
    ICalcModel,
    ICalcView,
)
from .model import CalcModel
from .view import CalcView


class CalculationModule(Module):
    """Simple Math calculation page module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        # MVC model
        binder.bind(ICalcModel, to=CalcModel)
        binder.bind(ICalcView, to=CalcView)
        binder.bind(ICalcController, to=CalcController)

        # Sources
        binder.bind(IExerciseSelectionSource, to=ExerciseSelectionSource)
