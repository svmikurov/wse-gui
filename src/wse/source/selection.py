"""Exercise params source."""

from collections.abc import Iterable

from toga.sources import ListSource, Row

# A long item name will break weights layout.
MAX_LENGTH_ITEM_NAME = 19
NAME_INDEX = 1


class SourceSelections(ListSource):
    """Custom source for selection widget."""

    def __init__(
        self,
        accessors: Iterable[str],
        data: Iterable | None = None,
        value: str | int | None = None,
    ) -> None:
        """Construct selection source."""
        super().__init__(accessors, data)
        self._value = value

    def set_value(self, value: object) -> None:
        """Set value by default."""
        self._value = value

        for listener in self.listeners:
            vars(listener)['interface'].value = self.find(value)

    def update_data(
        self,
        data: list[int, str, None | str],
        value: str | int | None = None,
    ) -> None:
        """Update source items."""
        self.clear()

        for item in data:
            self.truncate_long_item_name(item)
            self.append(item)

    @property
    def value(self) -> Row:
        """Choice from selection."""
        self._value = vars(self.listeners[0])['interface'].value
        return self._value

    @staticmethod
    def truncate_long_item_name(item: list) -> None:
        """Truncate long item name."""
        if len(item[NAME_INDEX]) > MAX_LENGTH_ITEM_NAME:
            item[NAME_INDEX] = item[NAME_INDEX][0:MAX_LENGTH_ITEM_NAME] + '...'
