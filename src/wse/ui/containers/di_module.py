"""UI containers DI module."""

from typing import no_type_check

from injector import Binder, Module

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
from .presentation import PresentationContainerABC
from .presentation.container import PresentationContainer


class UIContainerModule(Module):
    """UI containers DI module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        # Login container
        binder.bind(LoginModelProto, to=LoginModel)
        binder.bind(LoginContainerProto, to=LoginContainer)
        binder.bind(LoginControllerProto, to=LoginController)

        # Presentation container
        binder.bind(PresentationContainerABC, to=PresentationContainer)
