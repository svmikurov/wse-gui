"""Custom switch."""

import toga
from toga.sources import Listener


class SwitchApp(toga.Switch, Listener):
    """Custom switch."""

    def __init__(self, *args, **kwargs) -> None:
        """Construct custom switch."""
        super().__init__(*args, **kwargs)

    def set_value(self, value: bool) -> None:
        """Set the initial value for the widget."""
        self.value = value
