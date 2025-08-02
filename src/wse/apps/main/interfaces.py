"""Defines protocols for Main application component interfaces."""

from typing import Protocol

from wse.core.interfaces import IRoutes


class IMainRoutes(IRoutes, Protocol):
    """Protocol for main application page routes."""
