"""Defines UI components injection container."""

from typing import no_type_check

from injector import Binder, Module

from .interfaces import (
    ILoginContainer,
    ILoginController,
    ILoginModel,
    INumPadContainer,
    INumPadController,
    INumPadModel,
)
from .login import LoginContainer, LoginController, LoginModel
from .numpad import NumPadContainer, NumPadController, NumPadModel


class ComponentsModule(Module):
    """UI components injection container."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure bindings."""
        # Numpad container
        binder.bind(INumPadModel, to=NumPadModel)
        binder.bind(INumPadContainer, to=NumPadContainer)
        binder.bind(INumPadController, to=NumPadController)

        # Login container
        binder.bind(ILoginModel, to=LoginModel)
        binder.bind(ILoginContainer, to=LoginContainer)
        binder.bind(ILoginController, to=LoginController)
