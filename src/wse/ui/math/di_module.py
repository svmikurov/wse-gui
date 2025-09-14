"""Mathe discipline UI layer DI module."""

from typing import no_type_check

from injector import Binder, Module
from typing_extensions import override

from .calculation.abc import CalculationViewABC, CalculationViewModelABC
from .calculation.state import CalculationViewModel
from .calculation.view import CalculationView
from .index.abc import MathIndexModelViewABC, MathIndexViewABC
from .index.state import MathIndexViewModel
from .index.view import MathIndexView


class MathUIModule(Module):
    """Math discipline UI layer DI module."""

    @no_type_check
    @override
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        # Math index
        binder.bind(MathIndexViewABC, to=MathIndexViewModel)
        binder.bind(MathIndexModelViewABC, to=MathIndexView)

        # Calculation
        binder.bind(CalculationViewModelABC, to=CalculationViewModel)
        binder.bind(CalculationViewABC, to=CalculationView)
