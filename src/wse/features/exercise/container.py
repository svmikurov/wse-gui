"""Dependency injection exercise package container."""

from dependency_injector import containers, providers

from wse.features.exercise.controller import ExerciseController
from wse.features.exercise.model import ExerciseModel
from wse.features.exercise.view import ExercisesView


class ExerciseContainer(containers.DeclarativeContainer):
    """Exercise package DI container."""

    user_model = providers.Dependency()
    navigator = providers.Dependency()

    exercises_model = providers.Factory(
        ExerciseModel,
    )
    main_exercise_view = providers.Factory(
        ExercisesView,
    )
    exercises_controller = providers.Factory(
        ExerciseController,
        model=exercises_model,
        view=main_exercise_view,
        navigator=navigator,
    )
