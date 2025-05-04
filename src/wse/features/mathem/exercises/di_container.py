"""Defines DI containers for Mathematical exercises."""

from dependency_injector import containers, providers

from wse.features.mathem.exercises import (
    AnswerChecker,
    MultiplicationExercise,
    TaskStorage,
    TextDisplayRenderer,
)
from wse.features.mathem.exercises.exercises import AddingExercise


class ExercisesContainer(containers.DeclarativeContainer):
    """Exercise container."""

    multiplication_exercise = providers.Factory(
        MultiplicationExercise,
    )
    adding_exercise = providers.Factory(
        AddingExercise,
    )
    task_conditions_storage = providers.Factory(
        TaskStorage,
    )
    exercise_render = providers.Factory(
        TextDisplayRenderer,
    )
    answer_checker = providers.Factory(
        AnswerChecker,
    )
