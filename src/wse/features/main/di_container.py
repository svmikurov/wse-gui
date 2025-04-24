"""Defines dependency injection containers for home package."""

from dependency_injector import containers, providers

from wse.core.navigation.navigation_id import NavigationID
from wse.features import main
from wse.features.main import PracticeController, PracticeModel, PracticeView


class MainContainer(containers.DeclarativeContainer):
    """Main pages container."""

    auth_service = providers.Dependency()
    api_client = providers.Dependency()
    content_box = providers.Dependency()
    subject = providers.Dependency()
    # Containers
    layer_container = providers.DependenciesContainer()

    # Account page
    account_model = providers.Factory(
        main.AccountModel,
        auth_service=auth_service,
        api_client=api_client,
        subject=subject,
    )
    account_view = providers.Factory(
        main.AccountView,
        content_box=content_box,
        subject=subject,
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
        api_client=api_client,
    )
    home_view = providers.Factory(
        main.HomeView,
        content_box=content_box,
        subject=subject,
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
        subject=subject,
        login_container=layer_container.login_container,
    )
    login_controller = providers.Factory(
        main.LoginController,
        model=login_model,
        view=login_view,
    )

    # Practice page
    practice_model = providers.Factory(
        PracticeModel,
        service_layer=layer_container.service_layer,
    )
    practice_view = providers.Factory(
        PracticeView,
        content_box=content_box,
        subject=subject,
    )
    practice_controller = providers.Factory(
        PracticeController,
        model=practice_model,
        view=practice_view,
    )

    # NavigationID routes
    routes = providers.Dict(
        {
            NavigationID.ACCOUNT: account_controller,
            NavigationID.HOME: home_controller,
            NavigationID.LOGIN: login_controller,
            NavigationID.PRACTICE: practice_controller,
        }
    )
