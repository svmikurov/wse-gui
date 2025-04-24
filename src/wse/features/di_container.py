"""Defines dependency injection containers for features package."""

from dependency_injector import containers, providers

from wse.features.foreign.di_container import ForeignContainer
from wse.features.main.containers.di_container import LayoutContainer
from wse.features.main.di_container import MainContainer
from wse.features.shared.observer import Subject
from wse.features.shared.ui_containers import BaseContent


class FeatureContainer(containers.DeclarativeContainer):
    """Features package container."""

    auth_service = providers.Dependency()
    api_client = providers.Dependency()

    # Styled general box for content
    content_box = providers.Factory(BaseContent)
    # The subject of observation in the Observer pattern
    subject = providers.Factory(Subject)

    # Layout general containers
    layout_container = providers.Container(
        LayoutContainer,
        content_box=content_box,
        subject=subject,
    )

    # Basic containers
    main = providers.Container(
        MainContainer,
        auth_service=auth_service,
        api_client=api_client,
        content_box=content_box,
        subject=subject,
        layout_container=layout_container,
    )
    foreign = providers.Container(
        ForeignContainer,
        content_box=content_box,
        subject=subject,
    )
