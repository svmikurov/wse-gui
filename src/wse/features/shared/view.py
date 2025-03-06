"""Defines base views for the application."""

import toga
from toga.constants import COLUMN
from toga.style import Pack


class StyleView(toga.Box):
    """Provides a base style for views."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the view."""
        super().__init__()
        self.style = Pack(
            direction=COLUMN,
            flex=1,
        )


class BaseView(StyleView):
    """Serves as the base class for all views."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the view."""
        super().__init__(*args, **kwargs)
