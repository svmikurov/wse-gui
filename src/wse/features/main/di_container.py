"""Defines dependency injection containers for home package."""

from dependency_injector import containers, providers

from wse.core.navigaion.navigation_id import NavigationID
from wse.features.main.home_ctrl import HomeController
from wse.features.main.home_view import HomeView


class MainContainer(containers.DeclarativeContainer):
    """Main pages container."""

    content_box = providers.Dependency()

    # Home page
    home_view = providers.Factory(HomeView, content_box=content_box)
    home_ctrl = providers.Factory(HomeController, view=home_view)

    # NavigationID routes
    routes = providers.Dict(
        {
            NavigationID.HOME: home_ctrl,
        }
    )
