"""Defines protocols for overridden widgets."""

from typing import Protocol


class DividerProto(Protocol):
    """Protocol for overridden divider interface."""


class FlexColumnStubProto(Protocol):
    """Protocol for flexible column direction box interface."""


class FlexRowStubProto(Protocol):
    """Protocol for flexible column direction box interface."""


class LabelProto(Protocol):
    """Protocol for label interface."""

    @property
    def text(self) -> str:
        """The text displayed by the label."""

    @text.setter
    def text(self, value: object) -> None: ...
