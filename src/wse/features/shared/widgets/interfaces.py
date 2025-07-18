"""Defines protocols for overridden widgets."""

from typing import Protocol


class IDivider(Protocol):
    """Protocol for overridden divider interface."""


class IFlexColumnStub(Protocol):
    """Protocol for flexible column direction box interface."""


class IFlexRowStub(Protocol):
    """Protocol for flexible column direction box interface."""


class ILabel(Protocol):
    """Protocol for label interface."""

    @property
    def text(self) -> str:
        """The text displayed by the label."""

    @text.setter
    def text(self, value: object) -> None: ...
