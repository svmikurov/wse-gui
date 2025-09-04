"""Defines Login page injector module."""

from typing import no_type_check

from injector import Binder, Module

from .controller import AuthController
from .model import AuthModel
from .protocols import (
    AuthControllerProto,
    AuthModelProto,
    AuthViewProto,
)
from .view import AuthView


class LoginModule(Module):
    """Login page injector module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(AuthModelProto, to=AuthModel)
        binder.bind(AuthViewProto, to=AuthView)
        binder.bind(AuthControllerProto, to=AuthController)
