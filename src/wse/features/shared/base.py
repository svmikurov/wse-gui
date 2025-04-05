"""Defines base classes of functions features."""

from dataclasses import dataclass
from enum import Enum

import toga
from toga.constants import COLUMN

from wse.features.settings import PADDING_SM
from wse.interface.ifeatures import IContent, IController, IModel, IView


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

        # Test ID
        self.test_id: str | None = None

    def __repr__(self) -> str:
        """Represent a view."""
        text = super().__repr__()
        return f'{text[:-1]}:{self.test_id}>'


@dataclass
class BaseController(IController):
    """Implementation of the base controller."""

    view: IView
    model: IModel | None = None

    def __post_init__(self) -> None:
        """Add sources."""
        self.view.subject.add_listener(self)
        if self.model:
            self.model.subject.add_listener(self)

    @property
    def content(self) -> IContent:
        """Return page content."""
        return self.view.content


class BaseButtonName(str, Enum):
    """Base class for creating button enumerations."""

    def __str__(self) -> str:
        """Return button text."""
        return self.value


class BaseContent(toga.Box):
    """Base class for creating content."""

    test_id: str | None
