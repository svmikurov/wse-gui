"""Defines protocols for widget containers interface."""

from typing import Protocol

from ..interfaces.icontent import IGetContent
from ..interfaces.iobserver import IAddObserver


class IContainer(
    IGetContent,
    IAddObserver,
    Protocol,
):
    """Protocol for comon widget container interface."""
