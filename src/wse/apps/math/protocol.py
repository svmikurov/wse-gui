"""Defines protocols for Mathematics app component interfaces."""

from typing import Protocol

from wse.core.interfaces import RoutesProto


class MathRoutesProto(RoutesProto, Protocol):
    """Protocol for Mathematics application page routes."""
