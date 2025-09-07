"""Screen rooters."""

from typing import no_type_check

from wse.apps.nav_id import NavID
from wse.feature.interfaces.icontent import GetContentProto

from .calculation import CalculationViewProto


class UIRoutes:
    """Screen routes DI module."""

    @property
    @no_type_check
    def routes(self) -> dict[NavID, GetContentProto]:
        """Get view."""
        return {
            NavID.CALCULATION: CalculationViewProto,
        }
