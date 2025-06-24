"""Defines injection binds module container."""

from typing import no_type_check

from injector import Binder, Module

from .containers import SimpleMathCalcContainer
from .contorller import SimpleCalcController
from .interfaces import (
    ISimpleCalcController,
    ISimpleCalcView,
    ISimpleMathCalcContainer,
)
from .view import SimpleCalcView


class SimpleCalculationPageModule(Module):
    """Simple Math calculation page."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(ISimpleCalcView, to=SimpleCalcView)
        binder.bind(ISimpleCalcController, to=SimpleCalcController)
        binder.bind(ISimpleMathCalcContainer, to=SimpleMathCalcContainer)
