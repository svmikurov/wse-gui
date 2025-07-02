"""Defines protocols for data source interfaces."""

from typing import Generic, Protocol, TypeVar

T = TypeVar('T')


class IEntry(Generic[T]):
    """Data-Transfer-Object representation of entry."""


class ISelectionSource(Protocol[T]):
    """Protocol for selection source."""

    def index(self, entry: IEntry[T]) -> int:
        """Return entry index in collection."""

    def add(self, entry: T) -> None:
        """Add entry."""

    def update(self, entries: list[T]) -> None:
        """Update selection data source with entries."""

    def clear(self) -> None:
        """Remove all entry from the data source."""
