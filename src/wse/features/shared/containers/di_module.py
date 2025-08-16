"""Defines UI containers injection module."""

from typing import no_type_check

from injector import Binder, Module

from .assigned import AssignedContainer
from .iabc.iassigned import IAssignedContainer
from .iabc.itop_bar import ITopBarContainer, ITopBarController
from .interfaces import (
    ILoginContainer,
    ILoginController,
    ILoginModel,
    INumPadContainer,
    INumPadController,
    INumPadModel,
    ITextTaskContainer,
)
from .login import LoginContainer, LoginController, LoginModel
from .numpad import NumPadContainer, NumPadController, NumPadModel
from .task_panel import TextTaskPanel
from .top_bar import TopBarContainer, TopBarController


class ContainerModule(Module):
    """UI containers injection module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure bindings."""
        binder.bind(ITextTaskContainer, to=TextTaskPanel)

        # Numpad container
        binder.bind(INumPadModel, to=NumPadModel)
        binder.bind(INumPadContainer, to=NumPadContainer)
        binder.bind(INumPadController, to=NumPadController)

        # Login container
        binder.bind(ILoginModel, to=LoginModel)
        binder.bind(ILoginContainer, to=LoginContainer)
        binder.bind(ILoginController, to=LoginController)

        # TopBar container
        binder.bind(ITopBarContainer, to=TopBarContainer)
        binder.bind(ITopBarController, to=TopBarController)

        # Assigned exercises container
        binder.bind(IAssignedContainer, to=AssignedContainer)
