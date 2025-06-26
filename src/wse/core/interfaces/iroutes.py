"""Defines protocol for page route."""

from typing import Protocol

from wse.features.interfaces.imvc import IPageController
from wse.features.subapps.nav_id import NavID


class IRoutes(Protocol):
    """Protocol for page route mapping navigation interface."""

    @property
    def routes(self) -> dict[NavID, IPageController]:
        """Get page route mapping."""
