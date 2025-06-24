"""Defines protocol for Stile interfaces."""

from typing import Protocol


class IStyle(Protocol):
    """Protocol for Style interface."""

    def update(self, **kwargs: dict[str, str | int]) -> None:
        """Update component style."""
