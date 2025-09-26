"""Defines protocols for overridden widgets."""

from typing import Protocol, Type

import toga

DividerType = Type[toga.Divider]
FlexColumnStubType = Type[toga.Box]
FlexRowStubType = Type[toga.Box]


class LabelProto(Protocol):
    """Protocol for label interface."""

    @property
    def text(self) -> str:
        """The text displayed by the label."""

    @text.setter
    def text(self, value: object) -> None: ...
