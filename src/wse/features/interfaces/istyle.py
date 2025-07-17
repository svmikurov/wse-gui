"""Defines protocol for Stile interfaces."""

from typing import Protocol


class IStyle(Protocol):
    """Protocol for Style interface."""

    def update(self, **kwargs: object) -> None:
        """Update component style."""

    @property
    def direction(self) -> str:
        """The widget`s style direction."""

    @direction.setter
    def direction(self, value: str) -> None: ...


class IStyleMixin(Protocol):
    """Protocol for style interface."""

    @property
    def style(self) -> IStyle:
        """The widget`s style."""

    @style.setter
    def style(self, style: IStyle) -> None: ...
