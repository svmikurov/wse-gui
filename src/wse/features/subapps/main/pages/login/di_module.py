"""Defines Login page injector module."""

from typing import no_type_check

from injector import Binder, Module

from .controller import LoginController
from .interfaces import ILoginController, ILoginView
from .view import LoginView


class LoginModule(Module):
    """Login page injector module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(ILoginView, to=LoginView)
        binder.bind(ILoginController, to=LoginController)
