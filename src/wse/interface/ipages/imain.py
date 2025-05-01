"""Defines protocol interfaces for main features components."""

from typing import Protocol

from wse.interface.ifeatures import IContainer, IModel, IView


class IloginContainer(IContainer, Protocol):
    """Protocol defining the interface for login container."""


class ILoginModel(IModel, Protocol):
    """Protocol defining the interface for login page model."""

    def login(self, username: str, password: str) -> None:
        """Authenticate the user."""


class ILoginView(IView, Protocol):
    """Protocol defining the interface for login page model."""

    login_container: IloginContainer
