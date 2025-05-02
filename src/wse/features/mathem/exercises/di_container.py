"""Defines DI containers for Mathematical exercises."""

from dependency_injector import containers, providers

from wse.features.mathem.exercises.answer_checkers import StrictAnswerChecker
from wse.features.mathem.exercises.calculations import MultiplicationExercise


class MathematicalExercisesContainer(containers.DeclarativeContainer):
    """Mathematical exercise container."""

    multiplication = providers.Factory(
        MultiplicationExercise,
    )
    strict_checker = providers.Factory(
        StrictAnswerChecker,
    )
