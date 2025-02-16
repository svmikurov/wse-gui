"""Custom source for switchers."""

from collections.abc import Iterable

import toga
from toga.sources import Source


class SourceSwitch(Source):
    """Custom source for switches."""

    def __init__(self, value: object = False, accessor: str = 'value') -> None:
        """Construct source."""
        super().__init__()
        self.accessor = accessor
        setattr(self, accessor, value)

    def set_value(self, item: bool) -> None:
        """Set the initial value for the widget."""
        self.notify('change', item=item)

    def update_value(self, widget: toga.Widget) -> None:
        """Update value of widget."""
        value = getattr(widget, self.accessor)
        setattr(self, self.accessor, value)

    def get_value(self) -> bool:
        """Return the value of widget."""
        return getattr(self, self.accessor)


class SourceProgressArray:
    """Progress sources array for progress switches."""

    PROGRESS_ALIASES = {
        'study': 'S',
        'repeat': 'R',
        'examination': 'E',
        'know': 'K',
    }

    def __init__(self) -> None:
        """Construct source array."""
        self.study = SourceSwitch()
        self.repeat = SourceSwitch()
        self.examination = SourceSwitch()
        self.know = SourceSwitch()

    def set_value(self, value: Iterable) -> None:
        """Set the initial value for widgets."""
        for name, alias in self.PROGRESS_ALIASES.items():
            attr = getattr(self, name)
            attr.notify('change', item=bool(alias in value))

    def get_value(self) -> list:
        """Return the value of widgets."""
        value = []
        for name, alias in self.PROGRESS_ALIASES.items():
            attr = getattr(self, name)
            if attr.get_value():
                value.append(alias)
        return value
