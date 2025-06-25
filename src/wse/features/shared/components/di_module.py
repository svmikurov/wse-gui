"""Defines UI components injection container."""

from typing import no_type_check

from injector import Binder, Module

from .interfaces import INumPadContainer, INumPadController, INumPadModel
from .numpad import NumPadContainer, NumPadController, NumPadModel


class ComponentsModule(Module):
    """UI components injection container."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure bindings."""
        binder.bind(INumPadModel, to=NumPadModel)
        binder.bind(INumPadContainer, to=NumPadContainer)
        binder.bind(INumPadController, to=NumPadController)
