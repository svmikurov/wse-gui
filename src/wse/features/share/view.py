"""Base view."""

import toga
from toga.constants import COLUMN
from toga.style import Pack

from wse.interfaces.iview import IView


class StyleView(toga.Box):
    """Base style view."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the view."""
        super().__init__()
        self.style = Pack(
            direction=COLUMN,
            flex=1,
        )


class BaseView(StyleView, IView):
    """Base view."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the view."""
        super().__init__(*args, **kwargs)
