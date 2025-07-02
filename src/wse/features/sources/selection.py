"""Defines toga Selection widget data source."""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from toga.sources import Source

from wse.features.sources.interfaces import IEntry

T = TypeVar('T')


class Entry(IEntry[T]):
    """Data-Transfer-Object representation of entry."""

    def __init__(
        self,
        entry: T,
    ) -> None:
        """Construct the DTO."""
        self.entry = entry
        self.accessor = 'undefined'


class BaseSelectionSource(Source, Generic[T], ABC):
    """Abstract base class of Selection data source."""

    _items: list[Entry[T]]

    def __init__(self) -> None:
        """Construct the source."""
        super().__init__()
        self._items = []

    @abstractmethod
    def _create_entry_dto(self, entry: T) -> Entry[T]:
        """Create DTO of entry."""

    def __getitem__(self, index: int) -> Entry[T]:
        """Get item from collection by index."""
        return self._items[index]

    def index(self, entry: Entry[T]) -> int:
        """Return entry index in collection."""
        return self._items.index(entry)

    def add(self, entry: T) -> None:
        """Add entry."""
        entry_dto = self._create_entry_dto(entry)
        self._items.append(entry_dto)
        self.notify(
            'insert',
            index=self._items.index(entry_dto),
            item=entry_dto,
        )

    def update(self, entries: list[T]) -> None:
        """Update selection data source."""
        self.clear()
        for entry in entries:
            self.add(entry)

    def clear(self) -> None:
        """Remove all entry from the data source."""
        self._items = []
        self.notify('clear')
