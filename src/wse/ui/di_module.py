"""UI layer DI module."""

from typing import no_type_check

from injector import Binder, Module
from typing_extensions import override

from .calculation import (
    CalculationModelViewProto,
    CalculationViewProto,
)
from .calculation.state import CalculationModelView
from .calculation.view import CalculationView
from .routes import UIRoutes


class UIModule(Module):
    """UI layer DI module."""

    @no_type_check
    @override
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(UIRoutes)
        binder.bind(CalculationModelViewProto, to=CalculationModelView)
        binder.bind(CalculationViewProto, to=CalculationView)
