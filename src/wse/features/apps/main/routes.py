"""Defines Main application navigation components."""

from typing import no_type_check

from injector import inject

from wse.features.apps.main.pages.home.interfaces import IHomeController
from wse.features.apps.nav_id import NavID
from wse.features.base import BaseRoutes
from wse.features.interfaces import IController


@inject
class MainRoutes(BaseRoutes):
    """Main application page routes."""

    @property
    @no_type_check
    def routes(self) -> dict[NavID, IController]:
        """Get page routes."""
        return {
            NavID.HOME: self._injector.get(IHomeController),
        }
