"""Defines navigation combined applications page routes."""

from dataclasses import dataclass
from typing import Any, Type, no_type_check

from injector import inject

from ..feature.interfaces.imvc import PageControllerProto
from .main.protocol import MainRoutesProto
from .math.protocol import MathRoutesProto
from .nav_id import NavID


@inject
@dataclass
class Routes:
    """Route mapping navigation ID with pages."""

    _main_routes: MainRoutesProto
    _math_routes: MathRoutesProto

    @property
    @no_type_check
    def routes(self) -> dict[NavID, Type[PageControllerProto[Any]]]:
        """Get page routes."""
        return {
            **self._main_routes.routes,
            **self._math_routes.routes,
        }
