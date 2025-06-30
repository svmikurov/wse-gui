"""Defines Feature features injection module."""

from typing import no_type_check

from injector import Binder, Module

from .exercise import SimpleCalcService
from .interfaces import ISimpleCalcService


class FeatureServicesModule(Module):
    """Feature services injection module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure bindings."""
        binder.bind(ISimpleCalcService, to=SimpleCalcService)
