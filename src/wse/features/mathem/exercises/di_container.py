"""Defines DI containers for Mathematical exercises."""

from dependency_injector import containers, providers

from wse.config.settings import FEATURES_CONFIG_PATH
from wse.features.mathem.exercises.exercise_switcher import ExerciseSwitcher
from wse.features.mathem.exercises.exercises import (
    AddingExercise,
    DivisionExercise,
    MultiplicationExercise,
    SubtractionExercise,
)
from wse.features.shared.enums.exercises import Exercises


class ExercisesContainer(containers.DeclarativeContainer):
    """Exercise container."""

    # Configuration

    exercise_config = providers.Configuration(
        yaml_files=[
            FEATURES_CONFIG_PATH / 'mathem.yaml',
        ]
    )

    # Container dependencies

    exercise_services = providers.DependenciesContainer()

    # Exercises

    adding_exercise = providers.Factory(
        AddingExercise,
        operand_generator=exercise_services.random_operand_generator,
        config=exercise_config,
    )
    division_exercise = providers.Factory(
        DivisionExercise,
        operand_generator=exercise_services.random_operand_generator,
        config=exercise_config,
    )
    multiplication_exercise = providers.Factory(
        MultiplicationExercise,
        operand_generator=exercise_services.random_operand_generator,
        config=exercise_config,
    )
    subtraction_exercise = providers.Factory(
        SubtractionExercise,
        operand_generator=exercise_services.random_operand_generator,
        config=exercise_config,
    )

    # Maps exercise types (Exercises enum)
    # to their provider implementations.
    exercises = providers.Dict(
        {
            Exercises.ADDING: adding_exercise,
            Exercises.DIVISION: division_exercise,
            Exercises.MULTIPLICATION: multiplication_exercise,
            Exercises.SUBTRACTION: subtraction_exercise,
        }
    )

    # Exercise switcher (singleton to preserve state)

    exercise_switcher = providers.Singleton(
        ExerciseSwitcher,
        _exercises=exercises,
    )

    # API

    task_conditions_storage = exercise_services.task_conditions_storage
    exercise_render = exercise_services.exercise_render
    answer_checker = exercise_services.answer_checker
