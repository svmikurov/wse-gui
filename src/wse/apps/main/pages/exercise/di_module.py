"""Defines DI module for Exercise completion page."""

from typing import no_type_check

from injector import Binder, Module

from .controller import ExerciseController
from .iabc import IExerciseController, IExerciseModel, IExerciseView
from .model import ExerciseModel
from .view import ExerciseView


class ExerciseModule(Module):
    """Exercise completion page module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(IExerciseModel, to=ExerciseModel)
        binder.bind(IExerciseView, to=ExerciseView)
        binder.bind(IExerciseController, to=ExerciseController)
