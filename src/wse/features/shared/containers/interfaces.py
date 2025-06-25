"""Defines protocols for common container interfaces."""

from typing import Protocol

from ...interfaces.icontainers import IContainer


class IIOTextContainer(IContainer, Protocol):
    """Protocol for I/O one line text container interface."""
