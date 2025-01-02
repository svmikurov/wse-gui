"""Custom source for switchers."""

import toga
from toga.sources import Source


class SourceSwitch(Source):
    """Custom source for switches."""

    def __init__(self, value: object = False, accessor: str = 'value') -> None:
        """Construct source."""
        super().__init__()
        self.accessor = accessor
        setattr(self, accessor, value)

    def set_value(self, value: bool) -> None:
        """Set the initial value for the widget."""
        self.notify('set_value', value=value)

    def update_value(self, widget: toga.Widget) -> None:
        """Update value of widget."""
        value = getattr(widget, self.accessor)
        setattr(self, self.accessor, value)

    def get_value(self) -> bool:
        """Return the value of widget."""
        return getattr(self, self.accessor)
