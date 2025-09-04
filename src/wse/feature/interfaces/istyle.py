"""Defines protocol for style interfaces."""

from typing import Protocol


class StyleProto(Protocol):
    """Protocol for Style interface."""

    def update(self, **kwargs: object) -> None:
        """Update component style."""

    @property
    def direction(self) -> str:
        """The widget`s style direction."""

    @direction.setter
    def direction(self, value: str) -> None: ...


class StyleMixinProto(Protocol):
    """Protocol for style interface."""

    @property
    def style(self) -> StyleProto:
        """The widget`s style."""

    @style.setter
    def style(self, style: StyleProto) -> None: ...
