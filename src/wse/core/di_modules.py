"""Defines core injector module container."""

from typing import no_type_check

from injector import Binder, Module, singleton

from .auth.service import AuthService
from .interfaces import INavigator
from .interfaces.iauth import IAuthService
from .navigation.navigator import Navigator


class CoreModule(Module):
    """Core injector module container."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure dependencies."""
        binder.bind(INavigator, to=Navigator, scope=singleton)
        binder.bind(IAuthService, to=AuthService)
