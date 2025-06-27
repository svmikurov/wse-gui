"""Defines Main application navigation components."""

from typing import no_type_check

from injector import inject

from wse.features.base import BaseRoutes
from wse.features.interfaces import IPageController
from wse.features.subapps.main.pages.home.interfaces import IHomeController
from wse.features.subapps.main.pages.login.interfaces import ILoginController
from wse.features.subapps.nav_id import NavID


@inject
class MainRoutes(BaseRoutes):
    """Main application page routes."""

    @property
    @no_type_check
    def routes(self) -> dict[NavID, IPageController]:
        """Get page routes."""
        return {
            NavID.HOME: self._injector.get(IHomeController),
            NavID.LOGIN: self._injector.get(ILoginController),
        }
