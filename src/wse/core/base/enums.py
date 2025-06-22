"""Defines base class for enumerations."""

from enum import Enum


class BaseEnum(str, Enum):
    """Base class for enumerations."""

    value: str

    def __str__(self) -> str:
        """Return button text."""
        return self.value
