"""Defines Simple Math calculation page module."""

from typing import no_type_check

from injector import Binder, Module

from ...sources.interfaces import IExerciseSelectionSource
from ...sources.selection import ExerciseSelectionSource
from .controller import SimpleCalcController
from .interfaces import (
    ISimpleCalcController,
    ISimpleCalcModel,
    ISimpleCalcView,
)
from .model import SimpleCalcModel
from .view import SimpleCalcView


class SimpleCalculationModule(Module):
    """Simple Math calculation page module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        # MVC model
        binder.bind(ISimpleCalcModel, to=SimpleCalcModel)
        binder.bind(ISimpleCalcView, to=SimpleCalcView)
        binder.bind(ISimpleCalcController, to=SimpleCalcController)

        # Sources
        binder.bind(IExerciseSelectionSource, to=ExerciseSelectionSource)
