"""Defines protocols for Main application component interfaces."""

from typing import Protocol

from wse.core.interfaces import RoutesProto


class MainRoutesProto(RoutesProto, Protocol):
    """Protocol for main application page routes."""
