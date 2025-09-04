"""Defines Feature features injection module."""

from typing import no_type_check

from injector import Binder, Module

from .exercise import (
    AssignedService,
    CalculationService,
)
from .protocol import (
    AssignedServiceProto,
    CalculationServiceProto,
)


class FeatureServicesModule(Module):
    """Feature services injection module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure bindings."""
        binder.bind(CalculationServiceProto, to=CalculationService)
        binder.bind(AssignedServiceProto, to=AssignedService)
