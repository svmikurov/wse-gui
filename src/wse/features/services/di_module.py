"""Defines Feature features injection module."""

from typing import no_type_check

from injector import Binder, Module

from .exercise import CalcService
from .interfaces import ICalcService


class FeatureServicesModule(Module):
    """Feature services injection module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure bindings."""
        binder.bind(ICalcService, to=CalcService)
