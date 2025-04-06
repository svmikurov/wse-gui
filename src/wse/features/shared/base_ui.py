"""Defines base classes of functions features."""

import toga
from toga.constants import COLUMN

from wse.features.object_id import ObjectID
from wse.features.settings import PADDING_SM
from wse.interface.ifeatures import IContent


class BaseBox(toga.Box):
    """Base pages box.

    Defines a common style for derived box widgets.
    """

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the box."""
        super().__init__(*args, **kwargs)
        self.style.direction = COLUMN
        self.style.padding = PADDING_SM
        self.style.flex = 1

    def __repr__(self) -> str:
        """Represent a view."""
        text = super().__repr__()
        return f'{text[:-1]}:{self.id}>'


class BaseContent(IContent, BaseBox):
    """Base class for creating content."""

    @property
    def id(self) -> ObjectID | None:
        """Get the content test ID."""
        return self._id

    @id.setter
    def id(self, value: ObjectID) -> None:
        self._id = value
