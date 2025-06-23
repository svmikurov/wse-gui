"""Defines Mathematics application navigation components."""

from typing import no_type_check

from injector import inject

from wse.features.base import BaseRoutes
from wse.features.interfaces import IController
from wse.features.subapps.nav_id import NavID

from .pages.index.interfaces import IIndexMathController


@inject
class MathRoutes(BaseRoutes):
    """Mathematics application page routes."""

    @property
    @no_type_check
    def routes(self) -> dict[NavID, IController]:
        """Get page routes."""
        return {
            NavID.INDEX_MATH: self._injector.get(IIndexMathController),
        }
