"""Screen rooters."""

from typing import no_type_check

from wse.apps.nav_id import NavID
from wse.feature.interfaces.icontent import GetContentProto

from .main.account.abc import AuthViewABC
from .main.home.abc import HomeViewABC
from .math.calculation.protocol import CalculationViewProto
from .math.index.protocol import MathIndexViewProto


class UIRoutes:
    """Screen routes DI module."""

    @property
    @no_type_check
    def routes(self) -> dict[NavID, GetContentProto]:
        """Get view."""
        return {
            NavID.HOME: HomeViewABC,
            # Account
            NavID.LOGIN: AuthViewABC,
            # Mathematical discipline
            NavID.MATH_INDEX: MathIndexViewProto,
            NavID.CALCULATION: CalculationViewProto,
        }
