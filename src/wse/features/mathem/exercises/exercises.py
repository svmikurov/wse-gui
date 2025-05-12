"""Defines mathematical exercises."""

from wse.features.mathem.exercises.base.exercise import (
    SimpleCalculationExercise,
)
from wse.features.mathem.exercises.exercise_calculations import (
    AddAnswer,
    AddQuestion,
    DivAnswer,
    DivQuestion,
    MulAnswer,
    MulQuestion,
    SubAnswer,
    SubQuestion,
)
from wse.features.shared.enums.exercises import Exercises


class AddingExercise(SimpleCalculationExercise):
    """Adding exercise."""

    _exercise_type = Exercises.ADDING
    _question_class = AddQuestion
    _answer_class = AddAnswer


class DivisionExercise(SimpleCalculationExercise):
    """Division exercise."""

    _exercise_type = Exercises.DIVISION
    _question_class = DivQuestion
    _answer_class = DivAnswer


class MultiplicationExercise(SimpleCalculationExercise):
    """Multiplication exercise."""

    _exercise_type = Exercises.MULTIPLICATION
    _question_class = MulQuestion
    _answer_class = MulAnswer


class SubtractionExercise(SimpleCalculationExercise):
    """Subtraction exercise."""

    _exercise_type = Exercises.SUBTRACTION
    _question_class = SubQuestion
    _answer_class = SubAnswer
