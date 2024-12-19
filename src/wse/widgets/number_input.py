"""Custom NumberInput."""

from toga import NumberInput
from toga.sources import Listener


class NumberInputApp(NumberInput, Listener):
    """Custom NumberInput."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct custom NumberInput."""
        super().__init__(*args, **kwargs)

    def set_value(self, value) -> None:
        """Set the initial value."""
        self.value = value