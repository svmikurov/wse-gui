"""Defines dependency injection containers for features package."""

from dependency_injector import containers, providers

from wse.features.foreign.di_container import ForeignContainer
from wse.features.main.di_container import MainContainer
from wse.features.shared.ui_containers import BaseContent


class FeatureContainer(containers.DeclarativeContainer):
    """Features package container."""

    auth_service = providers.Dependency()

    # Styled general box for content
    content_box = providers.Factory(
        BaseContent,
    )

    main = providers.Container(
        MainContainer,
        content_box=content_box,
        auth_service=auth_service,
    )
    foreign = providers.Container(
        ForeignContainer,
        content_box=content_box,
    )
