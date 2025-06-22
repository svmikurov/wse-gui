"""Defines core injector module container."""

from typing import no_type_check

from injector import Binder, Module

from wse.core.interfaces import IRoutes
from wse.features.apps.routes import Routes


class FeaturesAppsModule(Module):
    """Core injector module container."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure dependencies."""
        binder.bind(IRoutes, to=Routes)
