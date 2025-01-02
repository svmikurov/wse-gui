"""Custom source for several switchers."""

from toga.sources import Source


class SourceSwitch(Source):
    """Custom source for several switches."""

    def __init__(self, value: bool = False) -> None:
        """Construct source."""
        super().__init__()
        self._value = value

    def set_value(self, value: bool) -> None:
        """Set the initial value for the widget."""
        self._value = value
        self.notify('set_value', value=value)

    def get_value(self) -> bool:
        """Return source value."""
        try:
            self.listeners[0]
        except IndexError:
            pass
        else:
            print(f'>>>>>>> {self.listeners[0].value = }')
        return self._value
