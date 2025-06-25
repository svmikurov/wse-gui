"""Defines protocol for Stile interfaces."""

from typing import Protocol


class IStyle(Protocol):
    """Protocol for Style interface."""

    def update(self, **kwargs: object) -> None:
        """Update component style."""


class IStyleMixin(Protocol):
    """Protocol for style interface."""

    @property
    def style(self) -> IStyle:
        """The button's style."""

    @style.setter
    def style(self, style: IStyle) -> None: ...
