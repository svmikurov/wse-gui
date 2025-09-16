"""Defines protocol for page route."""

from typing import Any, Protocol, Type

from wse.core.navigation.nav_id import NavID
from wse.feature.interfaces.imvc import NavigableView


class RoutesProto(Protocol):
    """Protocol for page route mapping navigation interface."""

    @property
    def routes(self) -> dict[NavID, Type[NavigableView[Any]]]:
        """Get page route mapping."""
