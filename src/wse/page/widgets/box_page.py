"""Base application page box with methods."""

import toga
from toga.style.pack import COLUMN

from wse.constants.settings import PADDING_SM
from wse.page.widgets.message import MessageMixin


class BaseBox(toga.Box):
    """Base page box.

    Defines a common style for derived box widgets.
    """

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the box."""
        super().__init__(*args, **kwargs)
        self.style.direction = COLUMN
        self.style.padding = PADDING_SM
        self.style.flex = 1


class WidgetMixin(MessageMixin):
    """General application page box."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the box."""
        super().__init__(*args, **kwargs)
