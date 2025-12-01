"""Word study params entities."""

from __future__ import annotations

from typing import TYPE_CHECKING

from toga.sources import Source

if TYPE_CHECKING:
    from wse.data.dto import foreign

# TODO: Replace module


class IdNameSource(Source):
    """ABC for Source for id-name entity."""

    def __init__(self) -> None:
        """Construct the source."""
        super().__init__()
        self._items: list[foreign.IdName] = []

    def __getitem__(self, index: int) -> foreign.IdName:
        """Get item from collection by index."""
        return self._items[index]

    def index(self, entry: foreign.IdName) -> int:
        """Return entry index in collection."""
        return self._items.index(entry)

    def add(self, entry: foreign.IdName) -> None:
        """Add entry."""
        self._items.append(entry)
        self.notify(
            'insert',
            index=self._items.index(entry),
            item=entry,
        )

    def update(self, entries: list[foreign.IdName]) -> None:
        """Update select data source."""
        self.clear()
        for entry in entries:
            self.add(entry)

    def clear(self) -> None:
        """Remove all entry from the data source."""
        self._items = []
        self.notify('clear')

    def find(self, entry: str) -> foreign.IdName:
        """Find entry in source entries."""
        for item in self._items:
            if item.name == entry:
                return item

        raise ValueError(
            f"{self.__class__.__name__} does not contain '{entry}' entry"
        )
