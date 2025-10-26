"""UI containers DI module."""

from typing import no_type_check

from injector import Binder, Module, SingletonScope

from .assigned import AssignationsContainerABC
from .assigned.container import AssignationsContainer
from .login import (
    LoginContainerABC,
    LoginControllerProto,
    LoginModelABC,
)
from .login.components import (
    LoginContainer,
    LoginController,
    LoginModel,
)
from .numpad import (
    NumPadContainer,
    NumPadContainerABC,
    NumPadController,
    NumPadControllerABC,
    NumPadModel,
    NumPadModelABC,
)
from .params import ParamsContainerABC, ParamsContainerModelABC
from .params.container import ParamsContainer, ParamsContainerModel
from .presentation.legacy import (
    PresentationContainerABC,
    PresentationContainerStateABC,
)
from .presentation.legacy.container import PresentationContainer
from .presentation.legacy.state import PresentationContainerState
from .presentation.presenter import LabelAccessorContainerABC
from .presentation.presenter.container import PresenterContainer
from .task_panel import TextTaskContainerABC, TextTaskPanel
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
        binder.bind(NumPadModelABC, to=NumPadModel)
        binder.bind(NumPadContainerABC, to=NumPadContainer)
        binder.bind(NumPadControllerABC, to=NumPadController)

        # Login container
        binder.bind(LoginModelABC, to=LoginModel)
        binder.bind(LoginContainerABC, to=LoginContainer)
        binder.bind(LoginControllerProto, to=LoginController)

        # Presentation container
        binder.bind(
            PresentationContainerStateABC,
            to=PresentationContainerState,
            scope=SingletonScope,
        )
        binder.bind(PresentationContainerABC, to=PresentationContainer)
        # Presenter
        binder.bind(LabelAccessorContainerABC, to=PresenterContainer)

        # Text task psnel
        binder.bind(TextTaskContainerABC, to=TextTaskPanel)

        # TopBar container
        binder.bind(TopBarContainerABC, to=TopBarContainer)
        binder.bind(TopBarControllerABC, to=TopBarController)

        # Params container
        binder.bind(ParamsContainerModelABC, to=ParamsContainerModel)
        binder.bind(ParamsContainerABC, to=ParamsContainer)
