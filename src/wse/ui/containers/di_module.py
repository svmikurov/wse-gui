"""UI containers DI module."""

from typing import no_type_check

from injector import Binder, Module

from .assigned import AssignationsContainerABC
from .assigned.container import AssignationsContainer
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
from .presentation import PresentationContainerABC
from .presentation.container import PresentationContainer
from .task_panel import TextTaskContainerProto, TextTaskPanel
from .top_bar import TopBarContainer, TopBarController
from .top_bar.abc import TopBarContainerABC, TopBarControllerABC


class UIContainerModule(Module):
    """UI containers DI module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        # Assiganation container
        binder.bind(AssignationsContainerABC, to=AssignationsContainer)

        # Numpad container
        binder.bind(NumpadModelProto, to=NumpadModel)
        binder.bind(NumpadContainerProto, to=NumpadContainer)
        binder.bind(NumpadControllerProto, to=NumpadController)

        # Login container
        binder.bind(LoginModelProto, to=LoginModel)
        binder.bind(LoginContainerProto, to=LoginContainer)
        binder.bind(LoginControllerProto, to=LoginController)

        # Presentation container
        binder.bind(PresentationContainerABC, to=PresentationContainer)

        # Text task psnel
        binder.bind(TextTaskContainerProto, to=TextTaskPanel)

        # TopBar container
        binder.bind(TopBarContainerABC, to=TopBarContainer)
        binder.bind(TopBarControllerABC, to=TopBarController)
