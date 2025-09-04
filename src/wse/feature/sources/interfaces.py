"""Defines protocols for data source interfaces."""

from typing import Generic, Protocol, TypeVar

T = TypeVar('T')


class EntryProto(Generic[T]):
    """Data-Transfer-Object representation of entry."""


class SelectSourceProto(Protocol[T]):
    """Protocol for select source."""

    def index(self, entry: EntryProto[T]) -> int:
        """Return entry index in collection."""

    def add(self, entry: T) -> None:
        """Add entry."""

    def update(self, entries: list[T]) -> None:
        """Update select data source with entries."""

    def clear(self) -> None:
        """Remove all entry from the data source."""
