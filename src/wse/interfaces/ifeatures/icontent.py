"""Defines protocol interfaces for content."""

from typing import Protocol

import toga

from wse.features.shared.enums import ObjectID

# fmt: off


class IContent(Protocol):
    """Protocol defining the interface for page content components."""
    @property
    def id(self) -> ObjectID | str:
        """Get the object test ID."""
    @id.setter
    def id(self, value: ObjectID) -> None:
        """Get the object test ID."""
    def add(self, *children: toga.Widget) -> None:
        """Add a widgets to page content."""
    @property
    def children(self) -> list[toga.Widget]:
        """The children of content node."""
