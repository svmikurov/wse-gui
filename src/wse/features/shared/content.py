"""Defines view content implementation."""

import toga
from injector import inject

from wse.config.layout import LayoutConfig
from wse.features.apps.nav_id import NavID


@inject
class Content(toga.Box):  # type: ignore[misc]
    """Page content."""

    def __init__(
        self,
        config: LayoutConfig,
    ) -> None:
        """Construct the content."""
        style = config.content_style
        style['direction'] = 'column'
        super().__init__(**style)
        self._test_id: NavID | None = None

    @property
    def test_id(self) -> NavID | None:
        """Get test ID."""
        return self._test_id

    @test_id.setter
    def test_id(self, value: NavID | None) -> None:
        self._test_id = value
