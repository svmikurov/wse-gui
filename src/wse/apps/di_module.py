"""Defines core injector module."""

from typing import no_type_check

from injector import Binder, Module

from wse.apps.routes import Routes
from wse.core.interfaces import IRoutes


class FeaturesAppsModule(Module):
    """Core injector module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure dependencies."""
        binder.bind(IRoutes, to=Routes)
