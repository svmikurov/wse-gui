"""Defines protocols for data source interfaces."""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class EntryProto(Generic[T]):
    """Data-Transfer-Object representation of entry."""


class SelectSourceABC(ABC, Generic[T]):
    """Protocol for select source."""

    @abstractmethod
    def index(self, entry: EntryProto[T]) -> int:
        """Return entry index in collection."""

    @abstractmethod
    def add(self, entry: T) -> None:
        """Add entry."""

    @abstractmethod
    def update(self, entries: list[T]) -> None:
        """Update select data source with entries."""

    @abstractmethod
    def clear(self) -> None:
        """Remove all entry from the data source."""
