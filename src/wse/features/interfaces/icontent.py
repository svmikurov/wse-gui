"""Defines protocols for page content interface."""

from typing import Protocol

from toga import Widget

from ..interfaces.istyle import IStyleMixin
from ..subapps.nav_id import NavID


class IContent(
    IStyleMixin,
    Protocol,
):
    """Protocol for content interface."""

    def add(self, *ui: Widget) -> None:
        """Add user interface to page content."""

    @property
    def test_id(self) -> NavID | None:
        """Get test ID of content."""

    @test_id.setter
    def test_id(self, value: NavID | None) -> None: ...

    @property
    def children(self) -> list[Widget]:
        """The children of content."""

    def replace(self, old_child: Widget, new_child: Widget) -> None:
        """Replace an existing child widget with a new child widget."""


class IGetContent(Protocol):
    """Protocol for get content interface."""

    @property
    def content(self) -> IContent:
        """Get page content."""
