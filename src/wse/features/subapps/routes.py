"""Defines navigation combined applications page routes."""

from dataclasses import dataclass
from typing import no_type_check

from injector import inject

from ..interfaces.imvc import IPageController
from .main.interfaces import IMainRoutes
from .mathematics.interfaces import IMathRoutes
from .nav_id import NavID


@inject
@dataclass
class Routes:
    """Route mapping navigation ID with pages."""

    _main_routes: IMainRoutes
    _math_routes: IMathRoutes

    @property
    @no_type_check
    def routes(self) -> dict[NavID, IPageController]:
        """Get page routes."""
        return {
            **self._main_routes.routes,
            **self._math_routes.routes,
        }
