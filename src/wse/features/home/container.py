"""Defines dependency injection containers for home package."""

from dependency_injector import containers, providers

from wse.features.home.controller import HomeController
from wse.features.home.view import HomeView


class MainContainer(containers.DeclarativeContainer):
    """Main pages container."""

    content_box = providers.Dependency()

    home_view = providers.Factory(HomeView, content_box=content_box)
    home_ctrl = providers.Factory(HomeController, view=home_view)
