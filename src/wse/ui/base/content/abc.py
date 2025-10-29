"""Abstract base class for page content."""

from abc import ABC, abstractmethod
from typing import Self

import toga
from toga.style import Pack

from wse.core.navigation.nav_id import NavID


class ContentABC(
    ABC,
):
    """ABC for content."""

    @abstractmethod
    def add(self, *ui: Self | toga.Widget) -> None:
        """Add widgets to page content."""

    @property
    @abstractmethod
    def test_id(self) -> NavID | None:
        """Get test ID of content."""

    @test_id.setter
    @abstractmethod
    def test_id(self, value: NavID | None) -> None: ...

    @property
    @abstractmethod
    def children(self) -> list[toga.Widget]:
        """Get widget children."""

    @property
    @abstractmethod
    def style(self) -> Pack:
        """Get widget style."""

    @abstractmethod
    def replace(
        self,
        old_child: Self | toga.Widget,
        new_child: Self | toga.Widget,
    ) -> None:
        """Replace an existing child widget with a new child widget."""

    @abstractmethod
    def insert(self, index: int, child: toga.Widget) -> None:
        """Insert a widget as a child of this widget."""

    @abstractmethod
    def clear(self) -> None:
        """Remove all child widgets of content."""

    @abstractmethod
    def get_by_id(self, widget_id: str) -> toga.Widget | None:
        """Get widget by widget ID."""


class GetContentABC(ABC):
    """ABC for to content."""

    @property
    @abstractmethod
    def content(self) -> ContentABC | toga.Widget:
        """Get content."""
