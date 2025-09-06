"""Defines Mathematics application navigation components."""

from typing import Any, Type, no_type_check

from wse.apps.nav_id import NavID
from wse.feature.base import BaseRoutes
from wse.feature.interfaces.imvc import PageControllerProto

from .pages.index import MathControllerProto
from .pages.simple_calc import CalculationControllerProto


class MathRoutes(BaseRoutes):
    """Mathematics application page routes."""

    @property
    @no_type_check
    def routes(self) -> dict[NavID, Type[PageControllerProto[Any]]]:
        """Get page routes."""
        return {
            NavID.INDEX_MATH: MathControllerProto,
            NavID.SIMPLE_CALC: CalculationControllerProto,
        }
