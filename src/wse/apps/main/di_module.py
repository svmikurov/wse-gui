"""Defines Main application module."""

from typing import no_type_check

from injector import Binder, Module

from .api import AssignationsApiProto
from .api.assignations import AssignationsApi
from .protocol import MainRoutesProto
from .routes import MainRoutes


class MainRoutesModule(Module):
    """Main application page route module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure binders."""
        binder.bind(MainRoutesProto, to=MainRoutes)
        binder.bind(AssignationsApiProto, to=AssignationsApi)
