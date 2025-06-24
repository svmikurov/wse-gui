"""Defines protocols for Main Math page components interface."""

from typing import Protocol

from wse.features.interfaces import IController, IView


class IIndexMathView(IView, Protocol):
    """Protocol for Main Math page view interface."""


class IIndexMathController(IController, Protocol):
    """Protocol for Main Math page controller interface."""
