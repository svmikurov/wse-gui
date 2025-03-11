"""Defines a Dependency Injection containers."""

from dependency_injector import containers, providers

from wse.core.auth.auth import AuthService
from wse.core.config import Settings
from wse.core.navigation.navigator import Navigator
from wse.features.auth.container import AuthContainer
from wse.features.auth.model import UserModel
from wse.features.exercise.container import ExerciseContainer
from wse.features.main.container import MainContainer


class CoreContainer(containers.DeclarativeContainer):
    """Core dependencies container."""

    settings = providers.Singleton(
        Settings,
    )
    user_model = providers.Factory(
        UserModel,
    )


class ServicesContainer(containers.DeclarativeContainer):
    """Services dependencies container."""

    settings = providers.Dependency()

    auth = providers.Singleton(
        AuthService,
        settings=settings,
    )


class FeaturesContainer(containers.DeclarativeContainer):
    """Provides dependencies for the application."""

    container = providers.Self()

    auth_service = providers.Dependency()
    user_model = providers.Dependency()

    navigator = providers.Singleton(
        Navigator,
        container=container,
    )

    # Package containers
    auth = providers.Container(
        AuthContainer,
        user_model=user_model,
        navigator=navigator,
    )
    main = providers.Container(
        MainContainer,
        user_model=user_model,
        navigator=navigator,
    )
    exercise = providers.Container(
        ExerciseContainer,
        user_model=user_model,
        navigator=navigator,
    )
