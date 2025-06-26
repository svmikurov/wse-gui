"""Defines protocols for widget containers interface."""

from typing import Protocol

from ..interfaces.icontent import IGetContent


class IContainer(
    IGetContent,
    Protocol,
):
    """Protocol for comon widget container interface."""
