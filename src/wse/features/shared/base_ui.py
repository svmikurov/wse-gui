"""Defines base widget classes with ID support and common styles."""

import toga
from toga.constants import COLUMN

from wse.features.object_id import ObjectID
from wse.features.settings import PADDING_SM


class IDWidgetMixin:
    """Mixin to add ID functionality to widgets.

    Provides an `id` property and enhances `repr()` to include the ID.
    """

    _id: ObjectID

    @property
    def id(self) -> ObjectID | None:
        """Get the widget's unique ID.

        Adds the `ObjectID` annotation to application widgets.
        Overrides the parent property.
        """
        return self._id

    @id.setter
    def id(self, value: ObjectID) -> None:
        # Set the widget's unique ID
        self._id = value

    def __repr__(self) -> str:
        """Return a string representation including the widget's ID.

        Overrides the parent method.
        """
        text = super().__repr__()
        return f'{text[:-1]}:{self.id}>'


class ColumnBox(IDWidgetMixin, toga.Box):
    """A box layout with vertical (column) direction."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Initialize the box with column direction."""
        super().__init__(*args, **kwargs)
        self.style.direction = COLUMN


class RowBox(IDWidgetMixin, toga.Box):
    """A box layout with horizontal (row) direction."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Initialize the box with row direction."""
        super().__init__(*args, **kwargs)


class RowFlexBox(RowBox):
    """A flexible box layout with horizontal (row) direction."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Initialize the box with flex styling."""
        super().__init__(*args, **kwargs)
        self.style.flex = 1


class ColumnFlexBox(ColumnBox):
    """A flexible box layout with vertical (column) direction."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Initialize the box with flex styling."""
        super().__init__(*args, **kwargs)
        self.style.flex = 1


class BaseBox(ColumnFlexBox):
    """Base box for pages with common settings."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Initialize the box with default padding."""
        super().__init__(*args, **kwargs)
        self.style.padding = PADDING_SM


class BaseContent(ColumnFlexBox):
    """Base class for content sections with ID support and styling."""
