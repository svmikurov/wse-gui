"""Custom switch."""

import toga
from toga.sources import Listener


class SwitchApp(toga.Switch, Listener):
    """Custom switch."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct custom switch."""
        super().__init__(*args, **kwargs)

    def change(self, item: object) -> None:
        """Set the initial value from data source for the widget."""
        self.value = item
