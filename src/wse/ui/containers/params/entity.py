"""Word study params entities."""

from __future__ import annotations

from typing import TYPE_CHECKING

from toga.sources import Source

if TYPE_CHECKING:
    from wse.api.foreign import requests

# TODO: Replace module


class IdNameSource(Source):
    """ABC for Source for id-name entity."""

    def __init__(self) -> None:
        """Construct the source."""
        super().__init__()
        self._items: list[requests.IdName] = []

    def __getitem__(self, index: int) -> requests.IdName:
        """Get item from collection by index."""
        return self._items[index]

    def index(self, entry: requests.IdName) -> int:
        """Return entry index in collection."""
        return self._items.index(entry)

    def add(self, entry: requests.IdName) -> None:
        """Add entry."""
        self._items.append(entry)
        self.notify(
            'insert',
            index=self._items.index(entry),
            item=entry,
        )

    def update(self, entries: list[requests.IdName]) -> None:
        """Update select data source."""
        self.clear()
        for entry in entries:
            self.add(entry)

    def clear(self) -> None:
        """Remove all entry from the data source."""
        self._items = []
        self.notify('clear')

    def find(self, entry: str) -> requests.IdName:
        """Find entry in source entries."""
        for item in self._items:
            if item.name == entry:
                return item

        raise ValueError(
            f"{self.__class__.__name__} does not contain '{entry}' entry"
        )
