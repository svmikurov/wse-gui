"""Defines Main Math page module container."""

from typing import no_type_check

from injector import Binder, Module

from .controller import IndexMathController
from .interfaces import IIndexMathController, IIndexMathView
from .view import IndexMathView


class IndexMathModule(Module):
    """Main Math page module container."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(IIndexMathView, to=IndexMathView)
        binder.bind(IIndexMathController, to=IndexMathController)
