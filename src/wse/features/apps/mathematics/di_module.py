"""Defines Mathematics application module container."""

from typing import no_type_check

from injector import Binder, Module

from .interfaces import IMathRoutes
from .routes import MathRoutes


class MathRoutesModule(Module):
    """Mathematics application page route module container."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure binders."""
        binder.bind(IMathRoutes, to=MathRoutes)
