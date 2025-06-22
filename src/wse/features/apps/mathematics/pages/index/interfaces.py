"""Defines protocols for Main Mathematical page component interfaces."""

from typing import Protocol

from wse.features.interfaces import IController, IView


class IIndexMathView(IView, Protocol):
    """Protocol for Main Mathematical page view interface."""


class IIndexMathController(IController, Protocol):
    """Protocol for Main Mathematical page controller interface."""
