"""Dependency Injection (DI) configuration for Mathematical feature."""

from dependency_injector import containers, providers

from wse.features.mathem.exercises.di_container import ExercisesContainer
from wse.features.mathem.exercises.servises.di_container import (
    ExerciseServicesContainer,
)
from wse.features.mathem.pages.di_container import MathematicalPagesContainer
from wse.features.mathem.subjects import (
    CalculationSubject,
    MathematicalSubject,
)


class MathematicalSubjectContainer(containers.DeclarativeContainer):
    """DI container for mathematical model subjects."""

    calculation_subject = providers.Factory(
        CalculationSubject,
    )
    mathematical_subject = providers.Factory(
        MathematicalSubject,
    )


class MathematicalContainer(containers.DeclarativeContainer):
    """DI container for mathematical feature components."""

    # Container dependencies

    share_container = providers.DependenciesContainer()

    # Sub-containers

    subject_container = providers.Container(
        MathematicalSubjectContainer,
    )
    exercise_services = providers.Container(
        ExerciseServicesContainer,
    )
    exercises_container = providers.Container(
        ExercisesContainer,
        exercise_services=exercise_services,
    )
    page_container = providers.Container(
        MathematicalPagesContainer,
        share_container=share_container,
        exercises_container=exercises_container,
        subject_container=subject_container,
    )

    # API

    routes = page_container.routes
