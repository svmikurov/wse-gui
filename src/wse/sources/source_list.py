"""Custom source list."""

from collections.abc import Iterable

from toga.sources import ListSource, Row

from wse.constants.settings import MAX_LINE_LENGTH
from wse.contrib.utils import add_line_break


class SourceListApp(ListSource):
    """Custom list source."""

    def __init__(
        self,
        *args: object,
        max_length: int = MAX_LINE_LENGTH,
        **kwargs: object,
    ) -> None:
        """Construct the source."""
        self.max_length = max_length
        super().__init__(*args, **kwargs)

    def append(self, entry: Iterable[str]) -> Row:
        """Add entry to source."""
        data = self.to_paragraph(entry)
        return self.insert(len(self), data)

    def truncate_long_item_name(self, items: Iterable[str]) -> list[str]:
        """Truncate long item."""
        result = []
        ellipsis_length = 2
        for item in items:
            if len(item) > self.max_length:
                truncate_length = self.max_length - ellipsis_length
                item = item[0:truncate_length] + '...'
            result.append(item)
        return result

    def to_paragraph(self, items: Iterable[str]) -> list[str]:
        """Create a readable text paragraph."""
        result = []
        for item in items:
            if len(item) > self.max_length:
                item = add_line_break(item, self.max_length)
            result.append(item)
        return result
