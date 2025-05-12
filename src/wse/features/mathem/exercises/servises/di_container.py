"""Defines DI containers for Mathematical exercise services."""

from dependency_injector import containers, providers

from wse.features.mathem.exercises.servises import (
    AnswerChecker,
    RandomOperandGenerator,
    TaskStorage,
    TextDisplayRenderer,
)


class ExerciseServicesContainer(containers.DeclarativeContainer):
    """Exercise services container."""

    task_conditions_storage = providers.Factory(
        TaskStorage,
    )
    exercise_render = providers.Factory(
        TextDisplayRenderer,
    )
    answer_checker = providers.Factory(
        AnswerChecker,
    )
    random_operand_generator = providers.Factory(
        RandomOperandGenerator,
    )
