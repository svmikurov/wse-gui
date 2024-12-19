"""Custom switch."""

import toga
from toga.sources import Listener


class SwitchApp(toga.Switch, Listener):
    """Custom switch."""

    def set_value(self, value: bool) -> None:
        """Set the initial value for the widget."""
        self.value = value
