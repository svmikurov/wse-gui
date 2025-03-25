"""Defines the general box styles."""

import toga
from toga.constants import COLUMN, ROW


class ColumnFlexBox(toga.Box):
    """A flex box with a column direction."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Initialize the box."""
        super().__init__(*args, **kwargs)
        self.style.flex = 1
        self.style.direction = COLUMN


class RowFlexBox(toga.Box):
    """A flex box with a row direction."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Initialize the box."""
        super().__init__(*args, **kwargs)
        self.style.flex = 1
        self.style.direction = ROW
