"""Defines dependency injection containers for home package."""

from dependency_injector import containers, providers

from wse.core.navigation.navigation_id import NavigationID
from wse.features import main
from wse.features.shared.observer import Subject


class MainContainer(containers.DeclarativeContainer):
    """Main pages container."""

    auth_service = providers.Dependency()
    content_box = providers.Dependency()

    subject = providers.Factory(
        Subject,
    )

    # Account page
    account_model = providers.Factory(
        main.AccountModel,
        subject=subject,
        auth_service=auth_service,
    )
    account_view = providers.Factory(
        main.AccountView,
        content_box=content_box,
    )
    account_controller = providers.Factory(
        main.AccountController,
        model=account_model,
        view=account_view,
    )

    # Home page
    home_model = providers.Factory(
        main.HomeModel,
        subject=subject,
    )
    home_view = providers.Factory(
        main.HomeView,
        content_box=content_box,
    )
    home_controller = providers.Factory(
        main.HomeController,
        view=home_view,
        model=home_model,
    )

    # Login page
    login_model = providers.Factory(
        main.LoginModel,
        subject=subject,
        auth_service=auth_service,
    )
    login_view = providers.Factory(
        main.LoginView,
        content_box=content_box,
    )
    login_controller = providers.Factory(
        main.LoginController,
        model=login_model,
        view=login_view,
    )

    # NavigationID routes
    routes = providers.Dict(
        {
            NavigationID.ACCOUNT: account_controller,
            NavigationID.HOME: home_controller,
            NavigationID.LOGIN: login_controller,
        }
    )
