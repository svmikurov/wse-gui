"""Defines Main Math page module."""

from typing import no_type_check

from injector import Binder, Module, multiprovider
from wse_exercises.base.enums import ExerciseEnum
from wse_exercises.core import MathExercise

from .controller import IndexMathController
from .interfaces import IIndexMathController, IIndexMathModel, IIndexMathView
from .model import IndexMathModel
from .view import IndexMathView


class IndexMathModule(Module):
    """Main Math page module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        # MVC dependencies
        binder.bind(IIndexMathModel, to=IndexMathModel)
        binder.bind(IIndexMathView, to=IndexMathView)
        binder.bind(IIndexMathController, to=IndexMathController)

    # Model dependencies

    @multiprovider
    def provide_exercises(self) -> list[ExerciseEnum]:
        """Provide the exercise list."""
        return [
            MathExercise.ADDING,
            MathExercise.SUBTRACTION,
            MathExercise.MULTIPLICATION,
            MathExercise.DIVISION,
        ]
