"""Defines protocol for Home page component interfaces."""

from typing import Protocol

from wse.features.interfaces import IView
from wse.features.interfaces.imvc import IPageController


class IHomeView(IView, Protocol):
    """Protocol for Home page view interface."""

    def add_observer(self, observer: object) -> None:
        """Subscribe observer an event has occurred."""


class IHomeController(IPageController, Protocol):
    """Protocol for Home page controller interface."""
