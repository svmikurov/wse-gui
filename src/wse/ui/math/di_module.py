"""Mathe discipline UI layer DI module."""

from typing import no_type_check

from injector import Binder, Module
from typing_extensions import override

from .calculation.protocol import (
    CalculationViewModelProto,
    CalculationViewProto,
)
from .calculation.state import CalculationViewModel
from .calculation.view import CalculationView
from .index.protocol import MathIndexViewModelProto, MathIndexViewProto
from .index.state import MathIndexViewModel
from .index.view import MathIndexView


class MathUIModule(Module):
    """Mathe discipline UI layer DI module."""

    @no_type_check
    @override
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        # Math index
        binder.bind(MathIndexViewModelProto, to=MathIndexViewModel)
        binder.bind(MathIndexViewProto, to=MathIndexView)

        # Calculation
        binder.bind(CalculationViewModelProto, to=CalculationViewModel)
        binder.bind(CalculationViewProto, to=CalculationView)
