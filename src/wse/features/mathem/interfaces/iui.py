"""Defines protocols for math UI."""

from typing import Protocol

from toga.sources import Source
from toga.widgets.selection import OnChangeHandler

# fmt: off


class ISourceSelection(Protocol):
    """Protocol for selection UI managed by the source."""
    _on_change: OnChangeHandler
    @property
    def items(self) -> Source:
        """The items to display in the selection."""
    @items.setter
    def items(self, items: Source) -> None: ...
    @property
    def on_change(self) -> OnChangeHandler:
        """Invoke when the value of the selection is changed."""
