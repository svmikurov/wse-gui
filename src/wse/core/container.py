"""Defines a Dependency Injection container for the application."""

from dependency_injector import containers, providers

from wse.core.app import WSE
from wse.core.auth.auth import AuthService
from wse.core.config import Settings
from wse.core.navigation.navigator import Navigator
from wse.features.auth.container import AuthContainer
from wse.features.auth.model import UserModel
from wse.features.exercise.container import ExerciseContainer
from wse.features.main.container import MainContainer


class DIContainer(containers.DeclarativeContainer):
    """Provides dependencies for the application."""

    container = providers.Self()

    # Settings
    settings = providers.Singleton(
        Settings,
    )

    # Services
    auth_service = providers.Singleton(
        AuthService,
        settings=settings,
    )
    navigator = providers.Singleton(
        Navigator,
        container=container,
    )

    # Application
    app = providers.Singleton(
        WSE,
        settings=settings,
        auth_service=auth_service,
        navigator=navigator,
    )

    # Models
    user_model = providers.Factory(
        UserModel,
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
