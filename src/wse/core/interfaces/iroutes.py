"""Defines protocol for page route."""

from typing import Protocol

from wse.features.apps.nav_id import NavID
from wse.features.interfaces import IController


class IRoutes(Protocol):
    """Protocol for page route mapping navigation interface."""

    @property
    def routes(self) -> dict[NavID, IController]:
        """Get page route mapping."""
