"""Word study params entities."""

from typing import NamedTuple

from toga.sources import Source

# TODO: Replace module


class NamedEntity(NamedTuple):
    """Named entity."""

    id: str
    name: str


MARKS: list[NamedEntity] = [
    NamedEntity('1', 'know'),
    NamedEntity('2', 'to study'),
    NamedEntity('3', 'repeat'),
]


CATEGORIES: list[NamedEntity] = [
    NamedEntity('1', 'color'),
    NamedEntity('2', 'django'),
    NamedEntity('3', 'rust'),
]


class NamedEntitySource(Source):
    """ABC for Source of named entity."""

    def __init__(self) -> None:
        """Construct the source."""
        super().__init__()
        self._items: list[NamedEntity] = []

    def __getitem__(self, index: int) -> NamedEntity:
        """Get item from collection by index."""
        return self._items[index]

    def index(self, entry: NamedEntity) -> int:
        """Return entry index in collection."""
        return self._items.index(entry)

    def add(self, entry: NamedEntity) -> None:
        """Add entry."""
        self._items.append(entry)
        self.notify(
            'insert',
            index=self._items.index(entry),
            item=entry,
        )

    def update(self, entries: list[NamedEntity]) -> None:
        """Update select data source."""
        self.clear()
        for entry in entries:
            self.add(entry)

    def clear(self) -> None:
        """Remove all entry from the data source."""
        self._items = []
        self.notify('clear')

    def find(self, entry: str) -> NamedEntity:
        """Find entry in source entries."""
        for item in self._items:
            if item.name == entry:
                return item

        raise ValueError(
            f"{self.__class__.__name__} does not contain '{entry}' entry"
        )
