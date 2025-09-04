"""Defines protocols for page content interface."""

from typing import Protocol

from toga import Widget

from wse.apps.nav_id import NavID

from ..interfaces.istyle import StyleMixinProto


class ContentProto(
    StyleMixinProto,
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

    def insert(self, index: int, child: Widget) -> None:
        """Insert a widget as a child of this widget."""

    def clear(self) -> None:
        """Remove all child widgets of content."""

    def get_by_id(self, widget_id: str) -> Widget | None:
        """Get widget by widget ID."""


class GetContentProto(Protocol):
    """Protocol for get content interface."""

    @property
    def content(self) -> ContentProto:
        """Get page content."""
