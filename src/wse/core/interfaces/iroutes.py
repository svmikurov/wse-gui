"""Defines protocol for page route."""

from typing import Protocol

from wse.apps.nav_id import NavID
from wse.features.interfaces.imvc import IPageController


class IRoutes(Protocol):
    """Protocol for page route mapping navigation interface."""

    @property
    def routes(self) -> dict[NavID, IPageController]:
        """Get page route mapping."""
