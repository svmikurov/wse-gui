"""Defines Home page module container."""

from typing import no_type_check

from injector import Binder, Module

from .controller import HomeController
from .interfaces import IHomeController, IHomeView
from .view import HomeView


class HomePageModule(Module):
    """Home page module container."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(IHomeView, to=HomeView)
        binder.bind(IHomeController, to=HomeController)
