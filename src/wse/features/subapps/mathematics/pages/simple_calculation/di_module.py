"""Defines injection binds module container."""

from typing import no_type_check

from injector import Binder, Module

from .containers import SimpleMathCalcContainer
from .contorller import SimpleCalcController
from .interfaces import (
    ISimpleCalcContainer,
    ISimpleCalcController,
    ISimpleCalcModel,
    ISimpleCalcView,
)
from .model import SimpleCalcModel
from .view import SimpleCalcView


class SimpleCalculationModule(Module):
    """Simple Math calculation page."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        # MVC model
        binder.bind(ISimpleCalcModel, to=SimpleCalcModel)
        binder.bind(ISimpleCalcView, to=SimpleCalcView)
        binder.bind(ISimpleCalcController, to=SimpleCalcController)
        # Page elements
        binder.bind(ISimpleCalcContainer, to=SimpleMathCalcContainer)
