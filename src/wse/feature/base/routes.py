"""Defines abstract base class for page routes."""

from abc import ABC, abstractmethod
from typing import Any

from injector import Injector, inject

from ...apps.nav_id import NavID
from ..interfaces.imvc import PageControllerProto


class BaseRoutes(ABC):
    """Abstract base class for page routes."""

    @inject
    def __init__(self, injector: Injector) -> None:
        """Construct page routes."""
        self._injector = injector

    @property
    @abstractmethod
    def routes(self) -> dict[NavID, PageControllerProto[Any]]:
        """Get the navigation ID mapping to page controllers.

        For example:
            @property
            @no_type_check
            def routes(self) -> dict[NavID, PageControllerProto]:
                return {
                    NavID.INDEX_MATH: self._injector.get(
                        MathControllerProto,
                    ),
                    ...,
                }
        """
