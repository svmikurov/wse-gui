"""Defines abstract base class for page routes."""

from abc import ABC, abstractmethod

from injector import Injector

from wse.features.interfaces import IController
from wse.features.subapps.nav_id import NavID


class BaseRoutes(ABC):
    """Abstract base class for page routes."""

    def __init__(
        self,
        injector: Injector,
    ) -> None:
        """Construct page routes."""
        self._injector = injector

    @property
    @abstractmethod
    def routes(self) -> dict[NavID, IController]:
        """Get page routes.

        For example:
            @property
            @no_type_check
            def routes(self) -> dict[NavID, IController]:
                return {
                    NavID.INDEX_MATH: self._injector.get(
                        IIndexMathController
                    ),
                    ...,
                }
        """
