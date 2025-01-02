"""Exercise params source."""

from collections.abc import Iterable

from toga.sources import ListSource, Row


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
            self.append(item)

    @property
    def value(self) -> Row:
        """Choice from selection."""
        self._value = vars(self.listeners[0])['interface'].value
        return self._value
