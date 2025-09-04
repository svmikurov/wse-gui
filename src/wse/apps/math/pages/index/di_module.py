"""Defines Main Math page module."""

from typing import no_type_check

from injector import Binder, Module, multiprovider
from wse_exercises.base.enums import ExerciseEnum
from wse_exercises.core import MathEnum

from .controller import MathController
from .model import MathModel
from .protocols import (
    MathControllerProto,
    MathModelProto,
    MathViewProto,
)
from .view import MathView


class MathModule(Module):
    """Index Math page module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        # MVC dependencies
        binder.bind(MathModelProto, to=MathModel)
        binder.bind(MathViewProto, to=MathView)
        binder.bind(MathControllerProto, to=MathController)

    # Model dependencies

    @multiprovider
    def provide_exercises(self) -> list[ExerciseEnum]:
        """Provide the exercises."""
        return [
            MathEnum.ADDING,
            MathEnum.SUBTRACTION,
            MathEnum.MULTIPLICATION,
            MathEnum.DIVISION,
        ]
