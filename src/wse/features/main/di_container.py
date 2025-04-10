"""Defines dependency injection containers for home package."""

from dependency_injector import containers, providers

from wse.core.navigation.navigation_id import NavigationID
from wse.features.main.home_controller import HomeController
from wse.features.main.home_model import HomeModel
from wse.features.main.home_view import HomeView
from wse.features.shared.observer import Subject


class MainContainer(containers.DeclarativeContainer):
    """Main pages container."""

    content_box = providers.Dependency()

    subject = providers.Factory(Subject)

    # Home page
    home_model = providers.Factory(HomeModel, subject=subject)
    home_view = providers.Factory(HomeView, content_box=content_box)
    home_controller = providers.Factory(
        HomeController, view=home_view, model=home_model
    )

    # NavigationID routes
    routes = providers.Dict(
        {
            NavigationID.HOME: home_controller,
        }
    )
