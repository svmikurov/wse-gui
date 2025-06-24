"""Defines protocols for widget containers interface."""

from typing import Protocol

from wse.features.interfaces.icontent import IGetContent
from wse.features.interfaces.iobserver import IAddObserver


class IContainer(
    IGetContent,
    IAddObserver,
    Protocol,
):
    """Protocol for comon widget container interface."""


class IIOTextContainer(IContainer, Protocol):
    """Protocol for I/O one line text container interface."""
