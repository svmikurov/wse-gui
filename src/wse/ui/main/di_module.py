"""Home screen UI layer DI module."""

from injector import Binder, Module

from wse.ui.main.home.abc import HomeViewABC, HomeViewModelABC
from wse.ui.main.home.state import HomeViewModel
from wse.ui.main.home.view import HomeView


class HomeModule(Module):
    """Home screen UI layer DI module."""

    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(HomeViewModelABC, to=HomeViewModel)  # type: ignore[type-abstract]
        binder.bind(HomeViewABC, to=HomeView)  # type: ignore[type-abstract]
