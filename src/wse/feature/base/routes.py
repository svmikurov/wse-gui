"""Defines abstract base class for page routes."""

from abc import ABC, abstractmethod
from typing import Any, Type

from ...apps.nav_id import NavID
from ..interfaces.imvc import PageControllerProto


class BaseRoutes(ABC):
    """Abstract base class for page routes."""

    @property
    @abstractmethod
    def routes(self) -> dict[NavID, Type[PageControllerProto[Any]]]:
        """Get the navigation ID mapping to page controllers.

        For example:
            @property
            @no_type_check
            def routes(self) -> dict[
                NavID,
                dict[NavID, Type[PageControllerProto[Any]]
            ]:
                return {
                    NavID.INDEX_MATH: MathControllerProto[...],
                    ),
                    ...,
                }
        """
