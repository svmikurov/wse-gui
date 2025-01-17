"""Application utils."""


def to_entries(items: list[dict]) -> list[tuple[str, ...]]:
    """Convert http response data to app source data.

    For example:

    >>> from wse.contrib.data import to_entries
    >>> http_response_data = [
    ...     {'id': 6, 'name': 'apple', 'color': 'green'},
    ...     {'id': 7, 'name': 'tomato', 'color': 'red'},
    ... ]
    >>> to_entries(http_response_data)
    [('6', 'apple', 'green'), ('7', 'tomato', 'red')]
    """
    return [tuple(map(str, item.values())) for item in items]


class SelectionEntries:
    """Convert response items to selection entries."""

    def __init__(self, json_data: dict[str, str | int | None]) -> None:
        """Construct entries."""
        self._items = self.to_items(json_data)

    @staticmethod
    def to_items(
        json_data: dict[str, str | int | None],
    ) -> list[dict[str, str | int | None]]:
        """Convert json data to items."""
        items = []
        for alias, humanly in json_data:
            item = {'alias': alias, 'humanly': humanly}
            items.append(item)
        return items

    @property
    def items(self) -> list:
        """Items for selection."""
        return self._items
