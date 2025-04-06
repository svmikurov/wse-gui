"""Defines dependency injection containers for core package."""

from dependency_injector import containers, providers

from wse.core.navigaion.navigator import Navigator


class CoreContainer(containers.DeclarativeContainer):
    """core package container."""

    navigator = providers.Singleton(Navigator)
