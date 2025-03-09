"""Defines a Dependency Injection container for the application."""

from dependency_injector import containers, providers

from wse.core.app import WSE
from wse.core.auth.auth import AuthService
from wse.core.config import Settings
from wse.core.navigation.navigator import Navigator
from wse.features.auth.controller import LoginController
from wse.features.auth.model import UserModel
from wse.features.main.controller import HomeController


class DIContainer(containers.DeclarativeContainer):
    """Provides dependencies for the application."""

    container = providers.Self()

    settings = providers.Singleton(
        Settings,
    )
    auth_service = providers.Singleton(
        AuthService,
        settings=settings,
    )
    navigator = providers.Singleton(
        Navigator,
        container=container,
    )

    app = providers.Singleton(
        WSE,
        settings=settings,
        auth_service=auth_service,
        navigator=navigator,
    )

    ####################################################################
    # Models

    user_model = providers.Factory(
        UserModel,
    )

    ####################################################################
    # Controllers

    home_controller = providers.Factory(
        HomeController,
        model=user_model,
        navigator=navigator,
    )
    login_controller = providers.Factory(
        LoginController,
        model=user_model,
        navigator=navigator,
    )
