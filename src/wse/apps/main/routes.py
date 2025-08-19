"""Defines Main application navigation components."""

from typing import no_type_check

from wse.apps.nav_id import NavID
from wse.features.base import BaseRoutes
from wse.features.interfaces.imvc import IPageController

from .pages.assigned.iabc import IAssignedController
from .pages.auth.interfaces import IAuthController
from .pages.exercise.iabc import IExerciseController
from .pages.home.interfaces import IHomeController


class MainRoutes(BaseRoutes):
    """Main application page routes."""

    @property
    @no_type_check
    def routes(self) -> dict[NavID, IPageController]:
        """Get page routes."""
        return {
            NavID.HOME: self._injector.get(IHomeController),
            NavID.LOGIN: self._injector.get(IAuthController),
            NavID.ASSIGNED: self._injector.get(IAssignedController),
            NavID.EXERCISE: self._injector.get(IExerciseController),
        }
