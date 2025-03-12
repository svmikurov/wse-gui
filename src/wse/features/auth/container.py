"""Dependency injection authentication package container."""

from dependency_injector import containers, providers

from wse.features.auth.controller import LoginController
from wse.features.auth.model import UserModel
from wse.features.auth.view import LoginView


class AuthContainer(containers.DeclarativeContainer):
    """Authentication package DI container."""

    auth_service = providers.Dependency()
    navigator = providers.Dependency()

    user_model = providers.Factory(
        UserModel,
        auth_service=auth_service,
    )
    login_view = providers.Factory(
        LoginView,
    )
    login_controller = providers.Factory(
        LoginController,
        model=user_model,
        view=login_view,
        navigator=navigator,
    )
