"""Defines Main application navigation components."""

from typing import no_type_check

from wse.apps.nav_id import NavID
from wse.feature.base import BaseRoutes
from wse.feature.interfaces.imvc import PageControllerProto

from .pages.assignations import AssignationsControllerProto
from .pages.assigned import AssignedControllerProto
from .pages.auth import AuthControllerProto
from .pages.home import HomeControllerProto


class MainRoutes(BaseRoutes):
    """Main application page routes."""

    @property
    @no_type_check
    def routes(self) -> dict[NavID, PageControllerProto]:
        """Get page routes."""
        return {
            NavID.HOME: self._injector.get(HomeControllerProto),
            NavID.LOGIN: self._injector.get(AuthControllerProto),
            NavID.ASSIGNED: self._injector.get(AssignationsControllerProto),
            NavID.EXERCISE: self._injector.get(AssignedControllerProto),
        }
