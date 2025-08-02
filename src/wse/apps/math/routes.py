"""Defines Mathematics application navigation components."""

from typing import no_type_check

from wse.apps.nav_id import NavID
from wse.features.base import BaseRoutes

from ...features.interfaces.imvc import IPageController
from .pages.index.interfaces import IIndexMathController
from .pages.simple_calc.interfaces import ISimpleCalcController


class MathRoutes(BaseRoutes):
    """Mathematics application page routes."""

    @property
    @no_type_check
    def routes(self) -> dict[NavID, IPageController]:
        """Get page routes."""
        return {
            NavID.INDEX_MATH: self._injector.get(IIndexMathController),
            NavID.SIMPLE_CALC: self._injector.get(ISimpleCalcController),
        }
