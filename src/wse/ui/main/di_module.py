"""Home screen UI layer DI module."""

from typing import no_type_check

from injector import Binder, Module

from .account.abc import AuthViewABC, AuthViewModelABC
from .account.state import AuthViewModel
from .account.view import AuthView
from .home.abc import HomeViewABC, HomeViewModelABC
from .home.state import HomeViewModel
from .home.view import HomeView


class HomeModule(Module):
    """Home screen UI layer DI module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(HomeViewModelABC, to=HomeViewModel)
        binder.bind(HomeViewABC, to=HomeView)
        binder.bind(AuthViewModelABC, to=AuthViewModel)
        binder.bind(AuthViewABC, to=AuthView)
