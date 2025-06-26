"""Defines protocols for overridden widgets."""

from typing import Protocol, runtime_checkable


@runtime_checkable
class IDivider(Protocol):
    """Protocol for overridden divider interface."""


class IFlexColumnStub(Protocol):
    """Protocol for flexible column direction box interface."""
