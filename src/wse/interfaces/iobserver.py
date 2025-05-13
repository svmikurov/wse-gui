"""Defines protocol interfaces for Observer pattern."""

from typing import Iterable, Protocol, TypeVar

import toga
from toga.sources import Listener, Source
from toga.widgets.selection import OnChangeHandler

from wse.features.shared.enums import FieldID
from wse.features.shared.enums.notify_id import NotifyID

# fmt: off

SourceT = TypeVar('SourceT', bound=Source)


class ISubject(Protocol):
    """An observable object in the Observer pattern."""
    def add_listener(self, listener: object) -> None:
        """Register an observer to receive notifications."""
    def notify(self, notification: str, **kwargs: object) -> None:
        """Register an observer to receive notifications."""


class ISubjectWithID(ISubject, Protocol):
    """Protocol for notify with component ID."""
    def notify_with_id(
        self,
        notify_id: NotifyID,
        field_id: FieldID | None = None,
        items: Iterable | None = None,
        value: object | None = None,
    ) -> None:
        """Notify observers about selection changes."""

class IListener(Listener, Protocol):
    """Protocol defining the interface for subject listener."""

class IStateSubject(Protocol):
    """Protocol defining the interface for a state change subject."""
    _on_change: OnChangeHandler
    @property
    def text(self) -> str: ...
    @property
    def value(self) -> str:
        """Get UI value."""
    @value.setter
    def value(self, value: str) -> None: ...
    @property
    def items(self) -> SourceT | Iterable | None: ...
    @items.setter
    def items(self, value: str) -> None: ...
    def change(self, value: str) -> None: ...
    def clean(self) -> None: ...
    @property
    def on_change(self) -> OnChangeHandler: ...
    @on_change.setter
    def on_change(self, handler: OnChangeHandler) -> None: ...
    @property
    def content(self) -> [toga.Widget]: ...
