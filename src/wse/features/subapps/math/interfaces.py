"""Defines protocols for Mathematics app component interfaces."""

from typing import Protocol

from wse.core.interfaces import IRoutes


class IMathRoutes(IRoutes, Protocol):
    """Protocol for Mathematics application page routes."""
