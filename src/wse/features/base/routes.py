"""Defines abstract base class for page routes."""

from abc import ABC, abstractmethod

from injector import Injector, inject

from ..interfaces.imvc import IPageController
from ..subapps.nav_id import NavID


class BaseRoutes(ABC):
    """Abstract base class for page routes."""

    @inject
    def __init__(self, injector: Injector) -> None:
        """Construct page routes."""
        self._injector = injector

    @property
    @abstractmethod
    def routes(self) -> dict[NavID, IPageController]:
        """Get the navigation ID mapping to page controllers.

        For example:
            @property
            @no_type_check
            def routes(self) -> dict[NavID, IPageController]:
                return {
                    NavID.INDEX_MATH: self._injector.get(
                        IIndexMathController
                    ),
                    ...,
                }
        """
