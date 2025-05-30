"""Defines dependency injection containers for main package."""

from dependency_injector import containers, providers

from wse.core.navigation.navigation_id import NavID
from wse.features import main


class MainContainer(containers.DeclarativeContainer):
    """Main pages container."""

    auth_service = providers.Dependency()
    api_client = providers.Dependency()
    content_box = providers.Dependency()
    subject = providers.Dependency()

    login_container = providers.Dependency()

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
        login_container=login_container,
    )
    login_controller = providers.Factory(
        main.LoginController,
        model=login_model,
        view=login_view,
    )

    # Education page
    education_model = providers.Factory(
        main.EducationModel,
        subject=subject,
    )
    education_view = providers.Factory(
        main.EducationView,
        content_box=content_box,
        subject=subject,
    )
    education_controller = providers.Factory(
        main.EducationController,
        model=education_model,
        view=education_view,
    )

    # NavigationID routes
    routes = providers.Dict(
        {
            NavID.ACCOUNT: account_controller,
            NavID.HOME: home_controller,
            NavID.LOGIN: login_controller,
            NavID.EDUCATION: education_controller,
        }
    )
