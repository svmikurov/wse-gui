"""Mathe discipline UI layer DI module."""

from typing import no_type_check

from injector import Binder, Module
from typing_extensions import override

from .calculation import (
    CalculationView,
    CalculationViewModel,
    CalculationViewModelProto,
    CalculationViewProto,
)


class MathUIModule(Module):
    """Mathe discipline UI layer DI module."""

    @no_type_check
    @override
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(CalculationViewModelProto, to=CalculationViewModel)
        binder.bind(CalculationViewProto, to=CalculationView)
