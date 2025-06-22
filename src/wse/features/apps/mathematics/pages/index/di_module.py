"""Defines Main Mathematical module container."""

from typing import no_type_check

from injector import Binder, Module

from .controller import IndexMathController
from .interfaces import IIndexMathController, IIndexMathView
from .view import IndexMathView


class IndexMathPageModule(Module):
    """Main Mathematical application page module container."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(IIndexMathView, to=IndexMathView)
        binder.bind(IIndexMathController, to=IndexMathController)
