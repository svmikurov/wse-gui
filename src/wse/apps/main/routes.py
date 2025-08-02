"""Defines Main application navigation components."""

from typing import no_type_check

from wse.apps.main.pages.auth.interfaces import IAuthController
from wse.apps.main.pages.home.interfaces import IHomeController
from wse.apps.nav_id import NavID
from wse.features.base import BaseRoutes
from wse.features.interfaces.imvc import IPageController


class MainRoutes(BaseRoutes):
    """Main application page routes."""

    @property
    @no_type_check
    def routes(self) -> dict[NavID, IPageController]:
        """Get page routes."""
        return {
            NavID.HOME: self._injector.get(IHomeController),
            NavID.LOGIN: self._injector.get(IAuthController),
        }
