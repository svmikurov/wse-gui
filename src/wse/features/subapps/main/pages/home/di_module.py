"""Defines Home page module."""

from typing import no_type_check

from injector import Binder, Module

from .controller import HomeController
from .interfaces import IHomeController, IHomeModel, IHomeView
from .model import HomeModel
from .view import HomeView


class HomeModule(Module):
    """Home page module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(IHomeModel, to=HomeModel)
        binder.bind(IHomeView, to=HomeView)
        binder.bind(IHomeController, to=HomeController)
