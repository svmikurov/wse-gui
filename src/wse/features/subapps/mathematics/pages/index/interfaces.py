"""Defines protocols for Main Math page components interface."""

from typing import Protocol

from wse.features.interfaces import IView
from wse.features.interfaces.imvc import IPageController


class IIndexMathView(IView, Protocol):
    """Protocol for Main Math page view interface."""


class IIndexMathController(IPageController, Protocol):
    """Protocol for Main Math page controller interface."""
