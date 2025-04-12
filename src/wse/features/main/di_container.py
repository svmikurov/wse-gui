"""Defines dependency injection containers for home package."""

from dependency_injector import containers, providers

from wse.core.navigation.navigation_id import NavigationID
from wse.features.main.account_controller import AccountController
from wse.features.main.account_view import AccountView
from wse.features.main.home_controller import HomeController
from wse.features.main.home_model import HomeModel
from wse.features.main.home_view import HomeView
from wse.features.main.login_controller import LoginController
from wse.features.main.login_model import LoginModel
from wse.features.main.login_view import LoginView
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

    # Account page
    account_view = providers.Factory(
        AccountView,
        content_box=content_box,
    )
    account_controller = providers.Factory(
        AccountController,
        view=account_view,
    )

    # Login page
    login_model = providers.Factory(
        LoginModel,
        subject=subject,
    )
    login_view = providers.Factory(
        LoginView,
        content_box=content_box,
    )
    login_controller = providers.Factory(
        LoginController,
        model=login_model,
        view=login_view,
    )

    # NavigationID routes
    routes = providers.Dict(
        {
            NavigationID.HOME: home_controller,
            NavigationID.ACCOUNT: account_controller,
            NavigationID.LOGIN: login_controller,
        }
    )
