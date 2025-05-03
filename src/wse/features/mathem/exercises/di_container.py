"""Defines DI containers for Mathematical exercises."""

from dependency_injector import containers, providers

from wse.features.mathem.exercises import (
    AnswerChecker,
    CheckResult,
    ExerciseRenderer,
    MultiplicationExercise,
    TaskConditions,
    TaskConditionsStorage,
)


class ExercisesContainer(containers.DeclarativeContainer):
    """Exercise container."""

    task_conditions = providers.Factory(
        TaskConditions,
    )
    multiplication_exercise = providers.Factory(
        MultiplicationExercise,
        _task_conditions=task_conditions,
    )
    task_conditions_storage = providers.Factory(
        TaskConditionsStorage,
    )
    exercise_render = providers.Factory(
        ExerciseRenderer,
    )
    check_result = providers.Factory(
        CheckResult,
    )
    answer_checker = providers.Factory(
        AnswerChecker,
        check_result=check_result,
    )
