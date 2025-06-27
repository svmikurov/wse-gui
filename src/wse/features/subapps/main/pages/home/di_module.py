"""Defines Home page module."""

from typing import no_type_check

from injector import Binder, Module

from .controller import HomeController
from .interfaces import IHomeController, IHomeView
from .view import HomeView


class HomeModule(Module):
    """Home page module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(IHomeView, to=HomeView)
        binder.bind(IHomeController, to=HomeController)
