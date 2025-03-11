"""Dependency injection authentication package container."""

from dependency_injector import containers, providers

from wse.features.auth.controller import LoginController
from wse.features.auth.view import LoginView


class AuthContainer(containers.DeclarativeContainer):
    """Authentication package DI container."""

    user_model = providers.Dependency()
    navigator = providers.Dependency()

    login_view = providers.Factory(
        LoginView,
    )
    login_controller = providers.Factory(
        LoginController,
        model=user_model,
        view=login_view,
        navigator=navigator,
    )
