"""Exercise params source."""

from collections.abc import Iterable

from toga.sources import ListSource, Row


class DefaultSource(ListSource):
    """Default source."""


class SourceItems(ListSource):
    """Exercise item source."""

    def __init__(
        self,
        accessors: Iterable[str],
        data: Iterable | None = None,
        value: str | int | None = None,
    ) -> None:
        """Construct selection source."""
        super().__init__(accessors, data)
        self._value = value

    def update_data(
        self,
        data: list[int, str, None | str],
        value: str | int | None = None,
    ) -> None:
        """Update source items."""
        self.clear()

        for item in data:
            self.append(item)

    def set_value(self, value: object) -> None:
        """Set value by default."""
        self._value = value

        for listener in self.listeners:
            listener.__dict__['interface'].value = self.find(value)

    @property
    def value(self) -> Row:
        """Choice from selection."""
        self._value = self.listeners[0].__dict__['interface'].value
        return self._value
