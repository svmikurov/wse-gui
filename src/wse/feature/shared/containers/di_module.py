"""Defines UI containers injection module."""

from typing import no_type_check

from injector import Binder, Module

from .assigned.abc import AssignationsContainerABC
from .assigned.container import AssignationsContainer
from .interfaces import TextTaskContainerProto
from .login import (
    LoginContainerProto,
    LoginControllerProto,
    LoginModelProto,
)
from .login.components import (
    LoginContainer,
    LoginController,
    LoginModel,
)
from .numpad import (
    NumpadContainer,
    NumpadContainerProto,
    NumpadController,
    NumpadControllerProto,
    NumpadModel,
    NumpadModelProto,
)
from .task_panel import TextTaskPanel
from .top_bar import TopBarContainer, TopBarController
from .top_bar.abc import TopBarControllerABC
from .top_bar.itop_bar import TopBarContainerProto


class ContainerModule(Module):
    """UI containers injection module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure bindings."""
        binder.bind(TextTaskContainerProto, to=TextTaskPanel)

        # Numpad container
        binder.bind(NumpadModelProto, to=NumpadModel)
        binder.bind(NumpadContainerProto, to=NumpadContainer)
        binder.bind(NumpadControllerProto, to=NumpadController)

        # Login container
        binder.bind(LoginModelProto, to=LoginModel)
        binder.bind(LoginContainerProto, to=LoginContainer)
        binder.bind(LoginControllerProto, to=LoginController)

        # TopBar container
        binder.bind(TopBarContainerProto, to=TopBarContainer)
        binder.bind(TopBarControllerABC, to=TopBarController)

        # Assigned exercises container
        binder.bind(AssignationsContainerABC, to=AssignationsContainer)
