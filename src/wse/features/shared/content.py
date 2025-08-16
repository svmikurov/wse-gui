"""Defines view content implementation."""

import toga
from injector import inject
from toga.widgets.base import Widget
from typing_extensions import override

from wse.apps.nav_id import NavID
from wse.config.layout import ThemeConfig

from ..interfaces.icontent import IContent


class Content(toga.Box, IContent):  # type: ignore[misc]
    """Page content."""

    @inject
    def __init__(
        self,
        theme_config: ThemeConfig,
    ) -> None:
        """Construct the content."""
        style = {
            **theme_config.content,
            'direction': 'column',
        }
        super().__init__(**style)
        self._test_id: NavID | None = None

    # TODO: Remove property, use `id` attribute
    @override
    @property
    def test_id(self) -> NavID | None:
        """Get test ID."""
        return self._test_id

    @test_id.setter
    def test_id(self, value: NavID | None) -> None:
        self._test_id = value

    def get_by_id(self, widget_id: str) -> Widget | None:
        """Get widget by widget ID."""
        child: Widget
        for child in self.children:
            if child.id == widget_id:
                return child
        return None
