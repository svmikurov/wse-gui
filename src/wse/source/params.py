"""Exercise params source."""

from toga.sources import ListSource, Row


class ChoiceRow(Row):
    """Choice row."""


class ParamSource(ListSource):
    """Exercise param source."""

    _data: list[ChoiceRow]

    def __init__(self, accessors, data):
        super().__init__(accessors, data)

    def update(self, params) -> None:
        """Update choices in source."""
        pass

