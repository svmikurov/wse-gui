"""DI module for Assigned exercise completion page."""

from typing import no_type_check

from injector import Binder, Module

from .controller import AssignedController
from .model import AssignedExerciseModel
from .protocol import AssignedControllerProto, AssignedModelProto


class ExerciseModule(Module):
    """Exercise completion page module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(AssignedModelProto, to=AssignedExerciseModel)
        binder.bind(AssignedControllerProto, to=AssignedController)
