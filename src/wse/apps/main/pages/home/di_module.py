"""DI module for Home page."""

from typing import no_type_check

from injector import Binder, Module

from .controller import HomeController
from .model import HomeModel
from .protocols import (
    HomeControllerProto,
    HomeModelProto,
    HomeViewProto,
)
from .view import HomeView


class HomeModule(Module):
    """Home page module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(HomeModelProto, to=HomeModel)
        binder.bind(HomeViewProto, to=HomeView)
        binder.bind(HomeControllerProto, to=HomeController)
