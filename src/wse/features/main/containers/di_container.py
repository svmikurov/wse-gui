"""Defines dependency injection containers for pages."""

from dependency_injector import containers, providers

from wse.features.main.containers.login import LoginContainer


class LayoutContainer(containers.DeclarativeContainer):
    """Layout containers for pages."""

    content_box = providers.Dependency()
    subject = providers.Dependency()

    # User login container
    login_container = providers.Factory(
        LoginContainer,
        content_box=content_box,
        subject=subject,
    )
