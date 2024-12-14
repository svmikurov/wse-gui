"""Exercise params source."""
from pygments.lexer import default
from toga.sources import ListSource, Row


class DefaultSource(ListSource):
    """"""


class ItemSource(ListSource):
    """Exercise item source."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default = 3

    def update_items(self, items: list[int, str, None | str]) -> None:
        """Update source items."""

        self.clear()
        for item in items:
            self.append(item)

        if self.default:
            self.listeners[-1].__dict__["interface"].value = self.find(self.default)

