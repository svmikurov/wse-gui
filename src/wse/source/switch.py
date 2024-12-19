"""Custom source for several switchers."""

from toga.sources import Source


class SourceSwitch(Source):
    """Custom source for several switches."""

    def __init__(self) -> None:
        """Construct the source."""
        super().__init__()

    def set_value(self, value: bool) -> None:
        """Set the initial value for the widget."""
        self.notify('set_value', value=value)
