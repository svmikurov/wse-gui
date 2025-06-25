"""Defines protocols for page content interface."""

from typing import Protocol

import toga

from wse.features.interfaces.istyle import IStyleMixin
from wse.features.subapps.nav_id import NavID


class IContent(
    IStyleMixin,
    Protocol,
):
    """Protocol for content interface."""

    def add(self, *ui: toga.Widget) -> None:
        """Add user interface to page content."""

    @property
    def test_id(self) -> NavID | None:
        """Get test ID of content."""

    @test_id.setter
    def test_id(self, value: NavID | None) -> None: ...


class IGetContent(Protocol):
    """Protocol for get content interface."""

    @property
    def content(self) -> IContent:
        """Get page content."""
