"""Defines dependency injection containers for pages."""

from dependency_injector import containers, providers

from wse.features.main.containers.login import LoginContainer
from wse.features.main.containers.service_layer import ServiceLayer


class LayerContainer(containers.DeclarativeContainer):
    """Layer container."""

    api_client = providers.Dependency()
    subject = providers.Dependency()
    context = providers.Dependency()
    content_box = providers.Dependency()

    # User login container
    login_container = providers.Factory(
        LoginContainer,
        content_box=content_box,
        subject=subject,
    )

    # Practice service layer
    service_layer = providers.Factory(
        ServiceLayer,
        api_client=api_client,
        subject=subject,
        context=context,
    )
