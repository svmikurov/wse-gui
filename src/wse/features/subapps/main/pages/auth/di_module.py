"""Defines Login page injector module."""

from typing import no_type_check

from injector import Binder, Module

from .controller import AuthController
from .interfaces import IAuthController, IAuthView
from .view import AuthView


class LoginModule(Module):
    """Login page injector module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(IAuthView, to=AuthView)
        binder.bind(IAuthController, to=AuthController)
