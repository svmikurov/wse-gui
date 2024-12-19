"""Custom NumberInput source."""

from decimal import Decimal

import toga
from toga.sources import Source


class SourceValue(Source):
    """Custom value source."""

    def __init__(self, value: object = None, accessor: str = 'value') -> None:
        """Construct source."""
        super().__init__()
        self.accessor = accessor
        setattr(self, accessor, value)

    def set_value(self, value: str | int | None = None) -> None:
        """Set the initial value for the widget."""
        self.notify('set_value', value=value)

    def update_value(self, widget: toga.Widget) -> None:
        """Update value."""
        value = getattr(widget, self.accessor)
        setattr(self, self.accessor, value)

    def get_value(self) -> str | int | None:
        """Get the value of widget."""
        value = getattr(self, self.accessor)
        if isinstance(value, Decimal):
            return int(value)
