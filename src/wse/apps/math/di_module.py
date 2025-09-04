"""Defines Mathematics application module."""

from typing import no_type_check

from injector import Binder, Module

from .protocol import MathRoutesProto
from .routes import MathRoutes


class MathAppModule(Module):
    """Math app module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure binders."""
        # Routes
        binder.bind(MathRoutesProto, to=MathRoutes)
