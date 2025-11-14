"""UI containers DI module."""

from typing import no_type_check

from injector import Binder, Module, SingletonScope

from . import numpad as np
from .assigned import AssignationsContainerABC
from .assigned.container import AssignationsContainer
from .control import ControlContainerABC
from .control.container import ControlContainer
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
from .params import ParamsContainerABC
from .params.container import ParamsContainer
from .presentation.legacy import (
    PresentationContainerABC,
    PresentationContainerStateABC,
)
from .presentation.legacy.container import PresentationContainer
from .presentation.legacy.state import PresentationContainerState
from .presentation.presenter import PresenterContainerABC
from .presentation.presenter.container import PresenterContainer
from .task_panel import TextTaskContainerABC, TextTaskPanel
from .top_bar import TopBarContainer, TopBarController
from .top_bar.abc import TopBarContainerABC, TopBarControllerABC


class UIContainerModule(Module):
    """UI containers DI module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        # Assignation container
        binder.bind(AssignationsContainerABC, to=AssignationsContainer)

        # NumPad container
        binder.bind(np.NumPadModelABC, to=np.NumPadModel)
        binder.bind(np.NumPadContainerABC, to=np.NumPadContainer)
        binder.bind(np.NumPadControllerABC, to=np.NumPadController)

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
        binder.bind(PresenterContainerABC, to=PresenterContainer)

        # Text task panel
        binder.bind(TextTaskContainerABC, to=TextTaskPanel)

        # TopBar container
        binder.bind(TopBarContainerABC, to=TopBarContainer)
        binder.bind(TopBarControllerABC, to=TopBarController)

        # Params container
        binder.bind(ParamsContainerABC, to=ParamsContainer)

        # Control container
        binder.bind(ControlContainerABC, to=ControlContainer)
