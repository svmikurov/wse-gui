"""Defines shared content boxes."""

import toga

from wse.features.shared.boxes import ColumnFlexBox, IDWidgetMixin


class BaseContent(ColumnFlexBox):
    """Base class for content sections with ID support and styling."""


class SimpleContent(IDWidgetMixin, toga.Box):
    """Simple content sections with ID support."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the content."""
        super().__init__(*args, **kwargs)
        self.style.direction = 'column'
