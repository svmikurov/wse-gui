"""Main package dependency injection container."""

from dependency_injector import containers, providers

from wse.features.main.controller import HomeController
from wse.features.main.view import HomeView


class MainContainer(containers.DeclarativeContainer):
    """Main package DI container."""

    user_model = providers.Dependency()
    navigator = providers.Dependency()

    home_view = providers.Factory(
        HomeView,
    )
    home_controller = providers.Factory(
        HomeController,
        model=user_model,
        view=home_view,
        navigator=navigator,
    )
