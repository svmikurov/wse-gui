"""Defines abstract base class for page routes."""

from abc import ABC, abstractmethod

from injector import Injector

from wse.features.apps.nav_id import NavID
from wse.features.interfaces import IController


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
        """Get page routes."""
