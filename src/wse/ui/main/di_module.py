"""Home screen UI layer DI module."""

from typing import no_type_check

from injector import Binder, Module

from .account.abc import AuthViewABC, AuthViewModelABC
from .account.state import AuthViewModel
from .account.view import AuthView
from .assignations.abc import AssignationsViewABC, AssignationsViewModelABC
from .assignations.state import AssignationsViewModel
from .assignations.view import AssignationsView
from .home.abc import HomeViewABC, HomeViewModelABC
from .home.state import HomeViewModel
from .home.view import HomeView


class HomeModule(Module):
    """Home screen UI layer DI module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        # Home screen
        binder.bind(HomeViewModelABC, to=HomeViewModel)
        binder.bind(HomeViewABC, to=HomeView)
        # Account screen
        binder.bind(AuthViewModelABC, to=AuthViewModel)
        binder.bind(AuthViewABC, to=AuthView)
        # Assigned exercises screen
        binder.bind(AssignationsViewModelABC, to=AssignationsViewModel)
        binder.bind(AssignationsViewABC, to=AssignationsView)
