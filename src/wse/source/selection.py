"""Custom selection source."""

from typing import Iterable

from toga.sources import ListSource


class SourceSelection(ListSource):
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
    ) -> None:
        """Update source items."""
        self.clear()

        for item in data:
            self.append(item)

    def set_value(self, value: object) -> None:
        """Set the initial value for the widget."""
        self.notify('set_value', value=value)
